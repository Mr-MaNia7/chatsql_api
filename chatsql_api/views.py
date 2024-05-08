from rest_framework.views import APIView
from rest_framework.response import Response
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from utils.db_conn import db
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool

from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

from dotenv import load_dotenv
load_dotenv()

from utils.environment import open_ai_model

class QueryView(APIView):
    def post(self, request, *args, **kwargs):
        # Generate query
        question = request.data.get("question")
        llm = ChatOpenAI(model=open_ai_model, temperature=0)
        generate_query = create_sql_query_chain(llm, db)
        query = generate_query.invoke({"question": question})

        # Execute query
        execute_query = QuerySQLDataBaseTool(db=db)
        result = execute_query.invoke(query)

        # Answer Style
        answer_prompt = PromptTemplate.from_template(
          """Given the following user question, corresponding SQL query, and SQL result, answer the user question
          Question: {question}
          SQL Query: {query}
          SQL Result: {result}
          Answer: """
        )

        rephrase_answer = answer_prompt | llm | StrOutputParser()

        chain = (
            RunnablePassthrough.assign(query=generate_query).assign(result=itemgetter("query") | 
              execute_query)| rephrase_answer)

        rephrased_answer = chain.invoke({"question": question})


        return Response({
            "query": query,
            "result": rephrased_answer
        })

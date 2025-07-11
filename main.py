from app.query import answer_question

while True:
    q = input("Ask : ")
    if q.lower() in ("exit" , "quite") : break
    print(answer_question(q))



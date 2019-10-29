from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)


project = Project(project_title=input(str()), summary=input(str()), link=input(str()))

db.session.add(project)
db. session.commit()

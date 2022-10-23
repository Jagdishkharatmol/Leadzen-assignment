from flask import Flask, url_for, render_template,request

app=Flask(__name__)


class todo:
    def __init__(self):
        self.all_task=[]
        self.complete_list=[]
        self.pending_list=[]

    def add_task(self,task):
        self.all_task.append(task)
        return 0

    def delete_task(self,task):
        self.all_task.remove(task)

    def complete_task(self,task):
        self.complete_list.append(task)
        self.complete_list
        return 0


    def list_pending(self):
        self.pending_list=[]
        for task in self.all_task:
            if task not in self.complete_list:
                self.pending_list.append(task)        
        return 0


todo_obj=todo()

@app.route('/')
def home():
    context={'all_task':todo_obj.all_task,'complete_list':todo_obj.complete_list,'pending_list':todo_obj.pending_list}
    return render_template('index.html',context=context)


@app.route('/<path:methods_name>/<path:value>',methods=["GET","POST"])
def home_todo(methods_name,value):
    if request.method=="POST":
        
        if methods_name=='create':
            task_name=request.form["task_name"]
            todo_obj.add_task(task_name)
            todo_obj.list_pending()
            
        elif methods_name=='delete':
            todo_obj.delete_task(value)
            todo_obj.list_pending()
            
        elif methods_name=="complete":
            todo_obj.complete_task(value)

        context={'all_task':todo_obj.all_task,'complete_list':todo_obj.complete_list,'pending_list':todo_obj.pending_list}
        return render_template('index.html',context=context)
    
    return "Wrong url"+ request.method


if __name__=='__main__':
    app.run()

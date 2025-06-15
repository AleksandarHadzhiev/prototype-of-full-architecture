function displayTodos(data) {
    const container = document.getElementById("container")
    data.forEach(todo => {
        const task = document.createElement('div');
        const text = document.createElement('p')
        const buttonsContainer = document.createElement('div')
        const editBtn = document.createElement('button')
        const removeBtn = document.createElement('button')
        removeBtn.setAttribute("id", todo.id)
        editBtn.setAttribute("id", todo.id)
        removeBtn.innerHTML = `<i class="fa fa-trash" aria-hidden="true"></i>`
        editBtn.innerHTML = `<i class="fa fa-pencil" aria-hidden="true"></i>`
        editBtn.addEventListener("click", function (e) {
            console.log(this.id); // logs the className of my_element
            edit(this.id, todo)
        })
        removeBtn.addEventListener("click", function (e) {
            console.log(this.id); // logs the className of my_element
            deleteTodo(this.id)
        })
        buttonsContainer.appendChild(editBtn)
        buttonsContainer.appendChild(removeBtn)
        task.classList.add('task')
        buttonsContainer.classList.add('buttons')
        console.log(buttonsContainer)
        console.log(task)
        text.innerText = todo.title;
        task.appendChild(text)
        task.appendChild(buttonsContainer)
        container.appendChild(task)
    });
}

function getTodoData() {
    const titleElement = document.getElementById("title")
    const title = String(titleElement.value).replace(" ", "") == "" ? null : titleElement.value

    const desc = document.getElementById("desc")
    const content = String(desc.value).replace(" ", "") == "" ? null : desc.value

    const dateToCompleteElement = document.getElementById("dateToComplete")

    const dateToComplete = String(dateToCompleteElement.value).replace(" ", "") == "" ? null : dateToCompleteElement.value
    const date = new Date(dateToComplete)
    const dateFormat = date.toLocaleString('nl-NL')
    if (content == null && dateToComplete == null) {
        return {
            title: title,
        }
    }
    else if (content == null && dateToComplete != null) {
        return {
            title: title,
            date_to_complete: dateFormat,
        }
    }
    else if (
        content != null && dateToComplete == null
    ) {
        return {
            title: title,
            content: content,
        }
    } else {
        return {
            title: title, content: content, date_to_complete: dateFormat,
        }
    }
}

function remove(id) {

}

function edit(id, todo) {
    const container = document.getElementById("container")
    const background = document.createElement('div');
    background.setAttribute('id', 'dialog-background')
    const dialog = document.createElement('div');
    dialog.setAttribute('id', 'dialog')
    dialog.addEventListener("click", function (e) {
        background.remove()
        dialog.remove()
    })
    const popup = document.createElement('form');
    popup.addEventListener("click", function (e) {
        e.stopPropagation()
        console.log('Popup has been clicked')
    })

    popup.addEventListener('submit', function (e) {
        e.preventDefault();
        editTodo(id);
    })
    generateForm(popup, todo)
    background.classList.add('background')
    dialog.classList.add('dialog')
    popup.classList.add('popup')
    dialog.appendChild(popup)
    container.appendChild(background)
    container.appendChild(dialog)
}

function generateForm(popup, task) {
    const formContent = `
        <div>
            <label for="title">Title</label>
            <input id="title" name="title" type="text" placeholder="${task.title}" value="${task.title}"/>
        </div>
        <div>
            <label for="desc">Description <span>(optional)</span></label>
            <input id="desc" name="desc" type="text"
                placeholder="${task.content}"
                value="${task.content}" />
        </div>
        <div>
            <label for="complete">Complete by: <span>(optional)</span></label>
            <input id="dateToComplete" name="complete" type="datetime-local" value="${task.date_to_complete}"/>
        </div>
        <div>
            <button>Submit</button>
            <a href="./index">Go back</a>
        </div>
        `
    popup.innerHTML = formContent
}

function getTodos() {
    fetch("/backend/todos/", { method: "GET" })
        .then(async (res) => {
            if (res.status == 200) {
                const data = await res.json()
                displayTodos(data)
            }
            else {
                const data = await res.json()
                console.log(data)
            }
        })
        .catch((err) => {
            alert(err)
        })
}

function deleteTodo(id) {
    fetch(`/backend/todos/${id}`, { method: "DELETE" })
        .then(async (res) => {
            if (res.status == 201) {
                const data = await res.json()
                alert(data.message)
            }
            else {
                const data = await res.json()
                alert(data)
            }
        })
        .catch((err) => {
            alert(err)
        })
}

function editTodo(id) {
    const todo = getTodoData()
    fetch(`/backend/todos/${id}`, { method: "PUT", body: JSON.stringify(todo) })
        .then(async (res) => {
            if (res.status == 201) {
                const data = await res.json()
                alert(data.message)
            }
            else {
                const data = await res.json()
                alert(data)
            }
        })
        .catch((err) => {
            alert(err)
        })
}

getTodos()
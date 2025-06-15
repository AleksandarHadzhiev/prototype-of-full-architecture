function displayTodos(data) {
    const container = document.getElementById("container")
    data.forEach(todo => {
        const task = document.createElement('div');
        const text = document.createElement('p')
        const buttonsContainer = document.createElement('div')
        const editBtn = document.createElement('button')
        const removeBtn = document.createElement('button')
        editBtn.textContent = "E"
        removeBtn.textContent = "D"
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

getTodos()
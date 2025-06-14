function displayTodos(data) {
    const container = document.getElementById("container")
    data.forEach(todo => {
        const task = document.createElement('div');
        const text = document.createElement('p')
        task.classList.add('task')
        text.innerText = todo.title;
        task.appendChild(text)
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
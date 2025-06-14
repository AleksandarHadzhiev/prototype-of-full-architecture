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

function createTodo() {
    const todo = getTodoData()
    fetch("/backend/todos/", { method: "POST", body: JSON.stringify(todo) })
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

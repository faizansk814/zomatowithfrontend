const container = document.getElementById("append")

function DisplayData() {
    fetch(`https://test-app-3ece.onrender.com/crud/get`)
        .then((res) => res.json())
        .then((data) => {
            fetchAndRender(data.data)
        })
        .catch((err) => console.log(err))
}
DisplayData()
function fetchAndRender(data) {

    data.forEach((ele) => {
        container.innerHTML = ""
        const div = document.createElement("div")
        div.classList.add("newdiv")
        let id = document.createElement("p")
        id.innerText = ` ID : ${ele.id}`
        let dishname = document.createElement('p')
        dishname.innerText = ` DISHNAME : ${ele.dishname}`
        let price = document.createElement('p')
        price.innerText = `PRICE : ${ele.price}`
        let available = document.createElement('p')
        available.innerText = `AVAILABLITY : ${ele.available}`
        let deletebutton=document.createElement('button')
        deletebutton.innerText="Delete"

        div.append(id, dishname, price, available)
        container.append(div)

    });

}
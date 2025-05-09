let tg = window.Telegram.WebApp;

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#FF8979"

let items = {
    lazanya: 0,
    zhylien: 0,
    karbonara: 0,
    hachapury: 0
}
let price = 0

let btn1 = document.querySelector("#btn1")
let btn2 = document.querySelector("#btn2")
let btn3 = document.querySelector("#btn3")
let btn4 = document.querySelector("#btn4")

let usercard = document.querySelector("#usercard")

function create_li(text) {
    let li = document.createElement("li")
    li.innerHTML = text
    usercard.appendChild(li)
}

function update_orders() {
    usercard.innerHTML = ""; // Очищаем список
    for (let item in items) {
        if (items[item] != 0) {
            create_li(item + ": " + items[item])
        }
    }
}

btn1.onclick = () => {
    items['lazanya'] += 1
    price += 5
    update_orders()
}

btn2.onclick = () => {
    items['zhylien'] += 1
    price += 3
    update_orders()
}

btn3.onclick = () => {
    items['karbonara'] += 1
    price += 4
    update_orders()
}

btn4.onclick = () => {
    items['hachapury'] += 1
    price += 6
    update_orders()
}

let submit = document.querySelector("#submit")

submit.onclick = () => {
    tg.MainButton.setText("Нажмите на кнопку для оформления заказа!")
    tg.MainButton.show()
}

Telegram.WebApp.onEvent("mainButtonClicked", function() {
    let result = "";
    result += "Ваши заказы:\n"
    for (let item in items) {
        if (items[item] != 0) {
            result += item + ": " + items[item] + "\n"
        }
    }
    result += "\n\nС вас " + price + "$"
    tg.sendData(result);
})

tg.expand();

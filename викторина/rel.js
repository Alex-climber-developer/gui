var i = 0;
var max_i = 3;
var at = 0;
var q1 = document.getElementById("question");
var a1 = document.getElementById("answer1");
var a2 = document.getElementById("answer2");
var a3 = document.getElementById("answer3");
var a4 = document.getElementById("answer4");
var a5 = document.getElementById("answer5");
var cn = document.getElementById("container");
var c2 = document.getElementById("c2");
const background = document.querySelector('body')
background.style.setProperty('background', bg[0])
var btn = document.getElementById('btn')
q1.innerHTML = questions[0].text;









function refresh(ind, ind2) {
    ind.innerHTML = questions[i].options[ind2 - 1];
}

function next() {
    i = i + 1;
    if (i < max_i) {
        a1.innerHTML = ''
        a2.innerHTML = ""
        a3.innerHTML = ""
        a4.innerHTML = ""
        a5.innerHTML = ""
        q1.innerHTML = questions[i].text;
        background.style.setProperty('background', bg[i])
    } else {
        if (i = max_i + 2) {
            background.style.setProperty('background', 'url("google-question.gif")');
            background.style.setProperty('background-position', 'center');
            a1.style.setProperty('display', 'none')
            a2.style.setProperty('display', 'none')
            a3.style.setProperty('display', 'none')
            a4.style.setProperty('display', 'none')
                // a5.style.setProperty('display', 'none')
            q1.style.setProperty('display', 'none')
            btn.style.setProperty('display', 'none')
            a5.innerHTML = 'Спасибо за внимание'
            a5.style.setProperty('margin-top', '500px')
                // a7.style.setProperty('color', 'rgb(0, 0, 0)')
            a5.style.setProperty('font-size', '90')
            a5.style.setProperty('background', '0')
            a5.style.setProperty('width', '100%')
            c2.style.setProperty('display', 'none')
            cn.style.setProperty('justify-content', 'center')
            cn.style.setProperty('padding-left', '0')

            // btn.style.setProperty('value', 'Вопрос дня')
            // btn.innerHTML = 'Вопрос дня'
        }
    }
}


a1.addEventListener("click", function() {
    refresh(a1, 1);
});

a2.addEventListener("click", function() {
    refresh(a2, 2);
});

a3.addEventListener("click", function() {
    refresh(a3, 3);
});

a4.addEventListener("click", function() {
    refresh(a4, 4);
});
a5.addEventListener("click", function() {
    refresh(a5, 5);
});
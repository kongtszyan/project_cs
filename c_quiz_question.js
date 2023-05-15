 /*  {
    "question": "What is the scientific name of a butterfly?",
    "answers": [
    "Apis",
    "Coleoptera",
    "Formicidae",
    "Rhopalocera"
    ],
    "correctIndex": 3
}*/
/*let q = {"Question": "Which approach would you adopt as an HR manager during a job interview?"};
let ans_txt = '{"Correct_ans":"Ask standarized questions for all candidates", "Incorrect_ans1":"Ask questions that encourage the candidates towards a desired answer"", "Incorrect_ans2":"Ask questions based on your preliminary assumptions", "Incorrect_ans3": "Ask questions that come to your mind" }';
let ans = JSON.parse(ans_txt);*/
//question = document.getElementByClassName("background").getElementById("display-container").getElementById("question").getElementById("header");

//fetch("c_quiz_question.json")
let obj = JSON.parse(`[{"question": "Which approach would you adopt as an HR manager during a job interview?", "correctAns": "Ask standarized questions for all candidates", "incorrectAns1": "Ask questions that encourage interviewee towards a desired answer", "incorrectAns2": "Ask questions based on your preliminary assumptions", "incorrectAns3": "Ask questions that come to your mind"}]`, 'utf-8');

console.log(obj);
question = document.querySelector("#header").innerHTML = obj[0].question;
choice1 = document.getElementById("option-1").innerHTML = obj[0].incorrectAns1;
choice2 = document.getElementById("option-2").innerHTML = obj[0].incorrectAns2;
choice3 = document.getElementById("option-3").innerHTML = obj[0].correctAns;
choice4 = document.getElementById("option-4").innerHTML = obj[0].incorrectAns3;



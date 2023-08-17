// function myFunction(x) {
//   x = document.querySelector(".dropbtn");
//   y = document.querySelector('.slide');
//   z = document.querySelector('.slide_1');
//   a = document.querySelector('.slide_2');
//   x.classList.toggle("change");
//   document.querySelector('.sidebar').classList.toggle('active');
// }

const add_el = document.querySelectorAll(".add_el");
const add_book = document.querySelector(".add-book");
const cover_div = document.querySelector(".cover-div");
const add = document.querySelector(".add");
const cancel = document.querySelectorAll(".cancel");
const overlay = document.querySelector(".overlay");
const register_div = document.querySelector('.register-div')
const add_book_div = document.querySelector('.add-book-div')
const signin_div = document.querySelector('.signin-div')
const all_divs = document.querySelectorAll('.divs')

function toggle_div(div_to_toggle) {
  div_to_toggle.classList.toggle("hidden");
}
add_el.forEach((el) => {
    el.addEventListener('click', function(event) {
        toggle_div(cover_div);
        toggle_div(overlay);
        if (el.classList.contains('register')) {
            toggle_div(register_div)
        }
        else if (el.classList.contains('signin')) {
            toggle_div(signin_div)
        }
        else if (el.classList.contains('add-book')) {
            toggle_div(add_book_div)
        }
    });
});


cancel.forEach((cancel_el) => {
    cancel_el.addEventListener('click', function() {
         all_divs.forEach((div) => {
             div.classList.add('hidden');
             toggle_div(cover_div);
             toggle_div(overlay);
         });
    });
});



//if (document.querySelector(".add-book")){
//add_book.addEventListener("click", function(){toggle_div(add_book_div)});}
//add.addEventListener("click", function(){toggle_div(add_book_div)});
//cancel.addEventListener("click", function(){toggle_div(add_book_div)});
//overlay.addEventListener("click", function(){toggle_div(add_book_div)});

// Show Register Div
//register_btn = document.querySelector('.register')

//cancel_register = document.querySelector('.cancel-register')
//register_btn.addEventListener("click", function(){toggle_div(register_div)});
//cancel_register.addEventListener("click", function(){toggle_div(register_div)});

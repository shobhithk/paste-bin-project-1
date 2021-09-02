var isloggedIn=false;
var signedup=false;
var isedit=false;
var isDelete=false;
var displayUrl;
document.getElementById("textbin").innerHTML="";
function loginFunc() {
    // document.getElementById("demo").innerHTML = "Hello World";
    console.log("h1")
    var uname;
    var paswd
    if (document.getElementById("name").value.trim() == "") {
      alert("Please enter name!");
      return false;
    }
    else{
      uname=document.getElementById("name").value.trim();
    }
    if (document.getElementById("passwd").value.trim() == "") {
      alert("Please enter proper password!");
      return false;
    }
    else{
       paswd=document.getElementById("name").value.trim();
    }

    localStorage.setItem("username", "ashi");
    alert("you are logged in successfully!");
    // if(uname=="ashi "&& paswd=="ashi"){
    // alert("you are logged in successfully!");
    // }
    // else{
    //   alert("enter correct username or password");
    // }
  }
  
  function signUpFunc() {
    // document.getElementById("demo").innerHTML = "Hello World";
    console.log("h3")
    
  }
  function editFunc() {
    // document.getElementById("demo").innerHTML = "Hello World";
    console.log("h4")
    var element = document.getElementById("url");
    element.classList.add("show");

  }
  function submitFunc() {
    // document.getElementById("demo").innerHTML = "Hello World";
    console.log("h5")
    if (document.getElementById("textbin").value.trim() == "") {
      alert("Please enter something!");
      return false;
    }
  }
  function deleteFunc() {
    // document.getElementById("demo").innerHTML = "Hello World";
    console.log("h6")
    var element = document.getElementById("url");
  element.classList.add("show");
  }

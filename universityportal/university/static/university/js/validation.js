function main()
{
    var status=true
    username=document.getElementById("txtname").value
    useremail=document.getElementById("txtemail").value
    userphone=document.getElementById("phonenumber").value
    userquery=document.getElementById("txtquery").value
    if(username.length==0)
    {
        document.getElementById("namemsg").innerHTML="*Name is Required"
        status=false
    }
    if(useremail.length==0)
    {
        document.getElementById("emailmsg").innerText="*Email is Required"
        status=false
    }
    if(userphone.length==0)
    {
        document.getElementById("phonemsg").innerText="*Phone Number Required"
        status=false
    }
    if(userquery.length==0)
    {
        document.getElementById("querymsg").innerText="*Enter your query"
        status=false
    }
    return status
}
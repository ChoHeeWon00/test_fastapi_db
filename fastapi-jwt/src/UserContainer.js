import { useState } from "react"

const path = "http://localhost:8000/users"
function MainCon(){

    const [token , setToken] = useState({token:"", token_type:""})

    async function onAddUser(){
        const user = {
            "username": "aaa", "password":"aaa"
        }
        const res = await fetch(path +"/signup", {
            method : "post",
            headers : {"content-type":"application/json"},
            body : JSON.stringify( user )
        } )
        console.log( await res.json() )
    }

    async function onSigin(){
        const user = {
            "username": "aaa", "password":"aaa"
        }
        const res = await fetch(path +"/signin", {
            method : "post",
            headers : {"content-type":"application/json"},
            body : JSON.stringify( user )
        } )
        setToken( await res.json() )
    }
    
    async function onInfo(){
        const res = await fetch(path+"/info/aaa",{
            method : "get",
            headers : {
                "content-type":"application/json",
                "Authorization":token["token_type"]+" "+token["token"]
            }
        })
        console.log("res => ", res)
        const result = await res.json()
        console.log("result => ", result)
    }
    return (<>
        token : {token["token"]} <br></br>
        token_type : {token["token_type"]} 
        <hr></hr>
        <button onClick={onAddUser}>aaa회원가입</button>
        <button onClick={onSigin}>aaa 로그인</button>
        <button onClick={onInfo}>aaa 개인정보 확인</button>
    </>)
}
export default MainCon


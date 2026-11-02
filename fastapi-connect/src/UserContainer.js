import { useState } from "react"

const path = "http://localhost:8000"

async function get_users(){
    const res = await fetch( path + "/users", {method:"get"} )
    console.log("res : ", res)
    if( res.ok ){ //성공적으로 통신 된다면
        //console.log( await res.json() )
        return await res.json()
    }
}
async function get_user( email ){
    //const res = await fetch( path + "/users/"+email, {method:"get"} )
    const res = await fetch( path + "/users/one/"+email, {method:"get"} )
    console.log("res : ", res)
    if( res.ok ){ //성공적으로 통신 된다면
        //console.log( await res.json() )
        //{un : aaa, pwd : aaa, em: ,,}
        return await res.json()
    }
    //return "문제발생"
}

async function del_user( username ){
    const res = await fetch( path + "/users/"+username, {method:"delete"} )
    console.log("res : ", res)
    return res.ok
    /*
    if( res.ok ){ //성공적으로 통신 된다면
        //console.log( await res.json() )
        //{un : aaa, pwd : aaa, em: ,,}
        return await res.json()
    }
    */
    //return "문제발생"
}


function MainCon(){
    //let num = 100
    //const [ num, setNum ] = useState(100)
    const [users, setUsers] = useState([])
    async function onAllUser(){
        //alert("실행???")
        //num = num + 1
        //setNum( num + 1 )
        //console.log("num : ", num)
        //console.log("get_users : ",await get_users() )
        const arr = [
            {username:"aaa",password:"aaa",
                 email:"aaa@aaa.aaa", name:"홍길동"},
            {username:"bbb",password:"bbb",
                 email:"bbb@bbb.bbb", name:"김개똥"},
        ]
        setUsers(await get_users())
    }

    const [email , setEmail ] = useState("")
    function onChangeEmail( e ){
        console.log( e.target.value )
        setEmail( e.target.value )
    }
    const [user , setUser ] = useState()
    async function onClickUser(){
        setUser( await get_user( email ) )
    }

    const [username , setUsername ] = useState("")
    function onChangeUsername( e ){
        console.log( e.target.value )
        setUsername( e.target.value )
    }
    //const [user , setUser ] = useState()
    //const onClickDelUser = async () => {}
    async function onClickDelUser(){
        let result = await del_user( username )  // res.ok : true, false
        if( result ){
            alert("삭제 성공!!")
        }
        else{
            alert("삭제 실패!!!")
        }
    }


    const [addUser, setAddUser] = useState({
        username : "", password:"", email:"", name:""
    })
    function onChangeAdd(e){
        console.log( e.target.name )
        console.log( e.target.value )
        //{ username : "aaa", password:"", email:"aaa@aaa.aaa", name:""}
        console.log( "저장전 : ",addUser )
        setAddUser({...addUser, [e.target.name] : e.target.value }) 
        
        console.log( addUser )
    }
    async function onAddSubmit( e ){
        e.preventDefault()
        console.log( e.target )
        console.log( typeof(addUser) )
        console.log( typeof( JSON.stringify(addUser)) )

        const res = await fetch( path + "/users" , {
            method :"post",
            headers : {"content-type":"application/json"},
            body :  JSON.stringify(addUser)
        })
        console.log("res : ", res)

    }

    const [userUpdate, setUserUpdate] = useState({
        name:"", email:"", username:""
    })
    function onChangeUpdate(e){
        setUserUpdate({...userUpdate, [e.target.name]:e.target.value })
    }
    async function onUpdateSubmit(e) {
        e.preventDefault()
        console.log( e.target )
        console.log( e.target.username )
        console.log( e.target.username.value )
        const formData = new FormData( e.target )
        const res = await fetch(path+"/users/form/"+e.target.username.value,{
            method : "put",
            body : formData
        })
        console.log("res : ", res)
    }

    return <>

        <form onSubmit={onUpdateSubmit} >
            username<input name="username" ></input><br></br>
            email<input name="email" ></input><br></br>
            name<input name="name" ></input><br></br>
            <button>저장</button>
        </form>


        <h3> - 개 인 정 보 - </h3>
        <form onSubmit={onAddSubmit} >
            username<input name="username" onChange={onChangeAdd}></input><br></br>
            password<input name="password" onChange={onChangeAdd} ></input><br></br>
            email<input name="email" onChange={onChangeAdd} ></input><br></br>
            name<input name="name" onChange={onChangeAdd} ></input><br></br>
            <button>저장</button>
        </form>
<hr></hr>


        <input type="email" onChange={onChangeUsername}></input><br></br>
        <button onClick={onClickDelUser}>삭제</button><br></br>

        <h3> - 개 인 정 보 - </h3>
        { user && (<>
            아이디 : {user.username}<br></br>
            비밀번호 : {user.password}<br></br>
            이메일 : {user.email}<br></br>
            이름 : {user.name}<br></br>
        </>)}
        
        <input type="email" onChange={onChangeEmail}></input><br></br>
        <button onClick={onClickUser}>개인 정보 확인</button><br></br>


        main 연동 num : {users.length}<br></br>
        <hr></hr>
            { users.map( ( user, idx ) => ( 
                <div key={idx}>
                    아이디 : {user.username}<br></br>
                    비밀번호 : {user.password}<br></br>
                    이메일 : {user.email}<br></br>
                    이름 : {user.name}<hr></hr>
                </div>
             ) ) }
        <hr></hr>
        <button onClick={onAllUser}>모든 목록 확인</button>
    </>
}





export default MainCon

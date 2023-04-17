import '../../../styles/Login.css'

import { useState, useContext, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { UserContext } from '../../../context/UserContext'
import { SignInUser } from '../../../services/Auth'
import { CheckSession } from '../../../services/Auth'

export default function Login() {
    const navigate = useNavigate()

    const { setLoggedIn, setUser } = useContext(UserContext)

    const [formValues, setFormValues] = useState({
        username: '',
        password: '',
    })

    const handleChange = (event) => {
        setFormValues({...formValues, [event.target.name]: event.target.value})
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const { user, ...payload } = await SignInUser(formValues, setUser)
            console.log(payload)
            setFormValues({ username: "", password: "" })
            setLoggedIn(true)
            localStorage.setItem('loggedIn', true)
            navigate("/")
            console.log("Logged In")
            setUser({ ...user, id: user })
        } catch (error) {
            console.error(error)
        }
    }

    useEffect(() => {
        const sessionData = CheckSession(setUser);
        if (sessionData) {
            setUser(sessionData.user)
            console.log('user', sessionData.user)
        }
    }, [])

    return (
        <div className='Login'>
            <form onSubmit={handleSubmit} className='loginform'>
                <div className='logininput'>
                    <label className='loginlabel'>Username:</label>
                    <input type="text" name="username" value={formValues.username} onChange={handleChange} />
                </div>
                <div className='logininput'>
                    <label className='loginlabel'>Password:</label>
                    <input type="password" name="password" value={formValues.password} onChange={handleChange} />
                </div>
                <button type="submit" className='login'>Login</button>
            </form>
            <Link to="/register" className='noaccount'> No Account? </Link>
        </div>
        
    )
}
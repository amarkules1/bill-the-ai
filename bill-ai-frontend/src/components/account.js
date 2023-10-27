import axios from 'axios';

export default class Account {
    constructor() {
        this.username = '';
        this.sessionToken = '';
        this.userId = '';
        this.email = '';
        this.tokenInvalid = false;
    }

    async isLoggedIn() {
        if (this.sessionToken !== '') {
            return true;
        }
        if (this.tokenInvalid) {
            return false;
        }
        let token = localStorage.getItem('token')
        if (token && token != "undefined") {
            try {
                let resp = await axios.post('/login', { token: token })
                this.username = resp.data.user_name
                this.email = resp.data.email
                this.sessionToken = resp.data.session_token
                this.userId = resp.data.user_id
                return true;
            } catch (err) {
                console.log(err)
                this.tokenInvalid = true;
                return false;
            }
        }
        return false;
    }

    async login (username, password) {
        try {
            let resp = await axios.post('/login', { email_user: username, password: password })
            this.username = resp.data.user_name
            this.email = resp.data.email
            this.sessionToken = resp.data.session_token
            this.userId = resp.data.user_id
            localStorage.setItem('token', resp.data.session_token)
            return true;
        } catch (err) {
            console.log(err)
            return false;
        }
    }

    async logout () {
        this.username = ''
        this.sessionToken = ''
        this.userId = ''
        localStorage.removeItem('token')
        this.tokenInvalid = true;
    }
        
}
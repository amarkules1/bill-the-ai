import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import SignupComponent from './components/SignupComponent.vue'
import QuestionsAndAnswers from './components/QuestionsAndAnswers.vue'
import UnsubComponent from './components/UnsubComponent.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/home', component: QuestionsAndAnswers },
        { path: '/signup', component: SignupComponent },
        { path: '/unsubscribe', component: UnsubComponent },
        { path: '/', redirect: '/home' }
    ]
})

createApp(App).use(router).mount('#app')

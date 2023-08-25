import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import SignupComponent from './components/SignupComponent.vue'
import QuestionsAndAnswers from './components/QuestionsAndAnswers.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/home', component: QuestionsAndAnswers },
        { path: '/performancetracker', component: SignupComponent },
        { path: '/', redirect: '/home' }
    ]
})

createApp(App).use(router).mount('#app')

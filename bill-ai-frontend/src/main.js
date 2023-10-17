import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import EmailSignupComponent from './components/EmailSignupComponent.vue'
import SignupComponent from './components/SignupComponent.vue'
import QuestionsAndAnswers from './components/QuestionsAndAnswers.vue'
import UnsubComponent from './components/UnsubComponent.vue'
import FeedbackComponent from './components/FeedbackComponent.vue'
import EmailVerificationComponent from './components/EmailVerificationComponent.vue'
import IntroComponent from './components/IntroComponent.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import ValidationProvider from 'vee-validate'

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/home', component: IntroComponent },
        { path: '/q_and_a/:bill_id', component: QuestionsAndAnswers },
        { path: '/email-signup', component: EmailSignupComponent },
        { path: '/signup', component: SignupComponent },
        { path: '/unsubscribe', component: UnsubComponent },
        { path: '/feedback', component: FeedbackComponent },
        { path: '/verify/:email/:id', component: EmailVerificationComponent },
        { path: '/', redirect: '/home' }
    ]
})

createApp(App).use(router).use(ValidationProvider).mount('#app')

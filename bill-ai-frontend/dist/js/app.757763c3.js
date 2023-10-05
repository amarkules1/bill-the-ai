(function(){"use strict";var e={7225:function(e,s,i){var l=i(9242),a=i(2483),n=i(3396);function t(e,s,i,l,a,t){const r=(0,n.up)("HeaderComponent"),o=(0,n.up)("router-view");return(0,n.wg)(),(0,n.iD)(n.HY,null,[(0,n.Wm)(r),((0,n.wg)(),(0,n.j4)(o,{key:e.$route.fullPath}))],64)}const r={id:"headerComponent"},o={class:"navbar navbar-expand-lg navbar-dark bg-dark header"},u={class:"container"},c=(0,n._)("a",{class:"navbar-brand title",href:""},"Bill The AI",-1),d=(0,n._)("button",{class:"navbar-toggler",type:"button","data-bs-toggle":"collapse","data-bs-target":"#navbarTogglerDemo02","aria-controls":"navbarTogglerDemo02","aria-expanded":"false","aria-label":"Toggle navigation"},[(0,n._)("span",{class:"navbar-toggler-icon"})],-1),m={class:"collapse navbar-collapse",id:"navbarTogglerDemo02"},b={class:"navbar-nav ms-auto"},h={class:"nav-item"},v={class:"nav-item"},p={class:"nav-item"},g={class:"nav-item"},f={class:"nav-item"},y={class:"nav-item"};function k(e,s,i,l,a,t){const k=(0,n.up)("router-link");return(0,n.wg)(),(0,n.iD)("div",r,[(0,n._)("nav",o,[(0,n._)("div",u,[c,d,(0,n._)("div",m,[(0,n._)("ul",b,[(0,n._)("li",h,[(0,n.Wm)(k,{class:"nav-link","active-class":"active",to:"/home"},{default:(0,n.w5)((()=>[(0,n.Uk)("Home")])),_:1})]),(0,n._)("li",v,[(0,n.Wm)(k,{class:"nav-link","active-class":"active",to:"/q_and_a/ira"},{default:(0,n.w5)((()=>[(0,n.Uk)("Inflation Reduction Act")])),_:1})]),(0,n._)("li",p,[(0,n.Wm)(k,{class:"nav-link","active-class":"active",to:"/q_and_a/fra"},{default:(0,n.w5)((()=>[(0,n.Uk)("Fiscal Responsibility Act")])),_:1})]),(0,n._)("li",g,[(0,n.Wm)(k,{class:"nav-link","active-class":"active",to:"/q_and_a/chips"},{default:(0,n.w5)((()=>[(0,n.Uk)("CHIPS and Science Act")])),_:1})]),(0,n._)("li",f,[(0,n.Wm)(k,{class:"nav-link","active-class":"active",to:"/signup"},{default:(0,n.w5)((()=>[(0,n.Uk)("Get Updates")])),_:1})]),(0,n._)("li",y,[(0,n.Wm)(k,{class:"nav-link","active-class":"active",to:"/feedback"},{default:(0,n.w5)((()=>[(0,n.Uk)("Give Feedback")])),_:1})])])])])])])}var _={name:"HeaderComponent"},w=i(89);const E=(0,w.Z)(_,[["render",k]]);var q=E,S={name:"App",components:{HeaderComponent:q}};const D=(0,w.Z)(S,[["render",t]]);var A=D,Q=i.p+"img/logo.8a5253ec.png";const U={class:"container"},x={class:"row"},C=(0,n._)("div",{class:"headshot col-md-3"},[(0,n._)("img",{alt:"Vue logo",src:Q})],-1),B={key:0,class:"subscribe col-md-8 form-group"},F=(0,n._)("h1",null,"Sign up for updates about Bill the AI!",-1),T=(0,n._)("p",null,"Enter your email to recieve updates about new features and improvements to Bill the AI.",-1),j=(0,n._)("br",null,null,-1),I={class:"emailBox"},O=["disabled"],V={key:1,class:"spinner-border",role:"status"},Z=(0,n._)("span",{class:"sr-only"},null,-1),W=[Z],H={key:1,class:"subscribe col-md-8"},Y=(0,n._)("h1",null,"Success",-1),R={key:2,class:"subscribe col-md-8"},P=(0,n._)("h1",null,"Error",-1),z=(0,n._)("p",null,"There was an issue saving your email, please try again later.",-1),M=[P,z];function $(e,s,i,a,t,r){const o=(0,n.up)("router-link"),u=(0,n.Q2)("validate");return(0,n.wg)(),(0,n.iD)("div",U,[(0,n._)("div",x,[C,t.isSuccess||t.isError?(0,n.kq)("",!0):((0,n.wg)(),(0,n.iD)("div",B,[F,T,j,(0,n._)("div",I,[(0,n.wy)((0,n._)("input",{type:"email",class:"form-control form-control-lg flex-grow-1 emailInput","onUpdate:modelValue":s[0]||(s[0]=e=>t.userEmail=e),placeholder:"Email"},null,512),[[u,"email"],[l.nr,t.userEmail]]),t.savingEmail?(0,n.kq)("",!0):((0,n.wg)(),(0,n.iD)("button",{key:0,class:"btn btn-info ml-2",onClick:s[1]||(s[1]=(...e)=>r.submitEmail&&r.submitEmail(...e)),disabled:t.userEmail.length<1},"Submit",8,O)),t.savingEmail?((0,n.wg)(),(0,n.iD)("div",V,W)):(0,n.kq)("",!0)])])),t.isSuccess?((0,n.wg)(),(0,n.iD)("div",H,[Y,(0,n._)("p",null,[(0,n.Uk)("You should receive a verification email from support@billtheai.com. Once you verify your email, we'll send you periodic updates about Bill the AI. You can unsubscribe at any time "),(0,n.Wm)(o,{to:"/unsubscribe"},{default:(0,n.w5)((()=>[(0,n.Uk)("here")])),_:1}),(0,n.Uk)(".")])])):(0,n.kq)("",!0),t.isError?((0,n.wg)(),(0,n.iD)("div",R,M)):(0,n.kq)("",!0)])])}var G=i(4161),K={name:"SignupComponent",data(){return{userEmail:"",isSuccess:!1,isError:!1,savingEmail:!1}},methods:{async submitEmail(){this.savingEmail=!0,this.loadingQuery=!0,G.Z.post("/subscribe",{email:this.userEmail}).then((()=>{this.isSuccess=!0,this.savingEmail=!1})).catch((()=>{this.isError=!0,this.savingEmail=!1}))}}};const L=(0,w.Z)(K,[["render",$]]);var N=L,J=i(7139);const X=(0,n._)("div",{class:"qaComponent"},null,-1),ee={key:0,class:"container introComponent"},se={class:"row"},ie=(0,n._)("div",{class:"headshot col-md-3"},[(0,n._)("img",{alt:"Vue logo",src:Q})],-1),le={class:"intro col-md-8"},ae=(0,n._)("p",null,[(0,n._)("a",{href:"{{billSummary.wiki_link}}"},"Wikipedia Link"),(0,n.Uk)("    "),(0,n._)("a",{href:"{{billSummary.full_text_link}}"},"Full Text")],-1),ne=(0,n._)("br",null,null,-1),te={class:"form-group d-flex queryBox"},re=["placeholder"],oe=["disabled"],ue={key:1,class:"spinner-border",role:"status"},ce=(0,n._)("span",{class:"sr-only"},null,-1),de=[ce],me={key:0,class:"spinner-border",role:"status"},be=(0,n._)("span",{class:"sr-only"},null,-1),he=[be],ve={key:1,class:"qnaContainer"},pe={class:"card-body"},ge=(0,n._)("strong",null,"Question:",-1),fe=(0,n._)("strong",null,"Answer:",-1);function ye(e,s,i,a,t,r){return(0,n.wg)(),(0,n.iD)(n.HY,null,[X,t.loadingSummary?(0,n.kq)("",!0):((0,n.wg)(),(0,n.iD)("div",ee,[(0,n._)("div",se,[ie,(0,n._)("div",le,[(0,n._)("h1",null,"Ask Bill a question about the "+(0,J.zw)(t.billSummary.bill_title),1),(0,n._)("p",null,(0,J.zw)(t.billSummary.summary),1),ae])])])),ne,(0,n._)("div",null,[(0,n._)("div",te,[(0,n.wy)((0,n._)("input",{type:"text",class:"form-control form-control-lg flex-grow-1 queryInput","onUpdate:modelValue":s[0]||(s[0]=e=>t.userQuery=e),placeholder:"Ask Bill a question about the "+t.billSummary.bill_title},null,8,re),[[l.nr,t.userQuery]]),t.loadingQuery?(0,n.kq)("",!0):((0,n.wg)(),(0,n.iD)("button",{key:0,class:"btn btn-info ml-2",onClick:s[1]||(s[1]=(...e)=>r.submitQuery&&r.submitQuery(...e)),disabled:t.userQuery.length<20},"Submit",8,oe)),t.loadingQuery?((0,n.wg)(),(0,n.iD)("div",ue,de)):(0,n.kq)("",!0)]),t.loadingQuestions?((0,n.wg)(),(0,n.iD)("div",me,he)):(0,n.kq)("",!0),t.loadingQuestions?(0,n.kq)("",!0):((0,n.wg)(),(0,n.iD)("div",ve,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(t.questionsAndAnswers,(e=>((0,n.wg)(),(0,n.iD)("div",{key:e.question,class:(0,J.C_)({selected:e.highlighted,card:!0,"mb-3":!0})},[(0,n._)("div",pe,[(0,n._)("p",null,[ge,(0,n.Uk)(" "+(0,J.zw)(e.question),1)]),(0,n._)("p",null,[fe,(0,n.Uk)(" "+(0,J.zw)(e.answer),1)])])],2)))),128))]))])],64)}var ke={name:"QuestionsAndAnswers",data(){return{userQuery:"",queryResult:null,questionsAndAnswers:[],loadingQuery:!1,loadingQuestions:!0,loadingSummary:!0,bill_id:"",billSummary:{}}},mounted(){let e=(0,a.yj)();this.bill_id=e.params.bill_id,this.fetchSummary(),this.fetchQuestionsAndAnswers()},methods:{async fetchQuestionsAndAnswers(){const e=await fetch(`/${this.bill_id}-q-and-a`);this.questionsAndAnswers=await e.json(),this.loadingQuestions=!1},async fetchSummary(){const e=await fetch(`/bill-summary?bill_id=${this.bill_id}`);this.billSummary=await e.json(),this.loadingSummary=!1},async submitQuery(){this.loadingQuery=!0;const e=await fetch(`/${this.bill_id}-query?query=${this.userQuery}`);this.queryResult=await e.json(),this.queryResult.highlighted=!0,this.questionsAndAnswers.unshift(this.queryResult),this.userQuery="",this.loadingQuery=!1}}};const _e=(0,w.Z)(ke,[["render",ye]]);var we=_e;const Ee={class:"container"},qe={class:"row"},Se=(0,n._)("div",{class:"headshot col-md-3"},[(0,n._)("img",{alt:"Vue logo",src:Q})],-1),De={key:0,class:"subscribe col-md-8 form-group"},Ae=(0,n._)("h2",null,"If you would like to unsubscribe, enter your email below.",-1),Qe=(0,n._)("br",null,null,-1),Ue={class:"emailBox"},xe=["disabled"],Ce={key:1,class:"spinner-border",role:"status"},Be=(0,n._)("span",{class:"sr-only"},null,-1),Fe=[Be],Te={key:1,class:"subscribe col-md-8"},je=(0,n._)("h1",null,"Success",-1),Ie={key:2,class:"subscribe col-md-8"},Oe=(0,n._)("h1",null,"Error",-1),Ve=(0,n._)("p",null,"There was an issue removing your email, please try again later or reach out to bill.the.ai.guy@gmail.com for support.",-1),Ze=[Oe,Ve];function We(e,s,i,a,t,r){const o=(0,n.up)("router-link"),u=(0,n.Q2)("validate");return(0,n.wg)(),(0,n.iD)("div",Ee,[(0,n._)("div",qe,[Se,t.isSuccess||t.isError?(0,n.kq)("",!0):((0,n.wg)(),(0,n.iD)("div",De,[Ae,Qe,(0,n._)("div",Ue,[(0,n.wy)((0,n._)("input",{type:"email",class:"form-control form-control-lg flex-grow-1 emailInput","onUpdate:modelValue":s[0]||(s[0]=e=>t.userEmail=e),placeholder:"Email"},null,512),[[u,"email"],[l.nr,t.userEmail]]),t.savingEmail?(0,n.kq)("",!0):((0,n.wg)(),(0,n.iD)("button",{key:0,class:"btn btn-info ml-2",onClick:s[1]||(s[1]=(...e)=>r.submitEmail&&r.submitEmail(...e)),disabled:t.userEmail.length<1},"Submit",8,xe)),t.savingEmail?((0,n.wg)(),(0,n.iD)("div",Ce,Fe)):(0,n.kq)("",!0)])])),t.isSuccess?((0,n.wg)(),(0,n.iD)("div",Te,[je,(0,n._)("p",null,[(0,n.Uk)("You've been unsubscribed from updates about Bill. You can sign back up "),(0,n.Wm)(o,{to:"/signup"},{default:(0,n.w5)((()=>[(0,n.Uk)("here")])),_:1}),(0,n.Uk)(".")])])):(0,n.kq)("",!0),t.isError?((0,n.wg)(),(0,n.iD)("div",Ie,Ze)):(0,n.kq)("",!0)])])}var He={name:"UnsubComponent",data(){return{userEmail:"",isSuccess:!1,isError:!1,savingEmail:!1}},methods:{async submitEmail(){this.savingEmail=!0,this.loadingQuery=!0,G.Z.post("/unsubscribe",{email:this.userEmail}).then((()=>{this.isSuccess=!0,this.savingEmail=!1})).catch((()=>{this.isError=!0,this.savingEmail=!1}))}}};const Ye=(0,w.Z)(He,[["render",We]]);var Re=Ye;const Pe={class:"container"},ze={class:"row"},Me=(0,n._)("div",{class:"headshot col-md-3"},[(0,n._)("img",{alt:"Vue logo",src:Q})],-1),$e={key:0,class:"subscribe col-md-8 form-group"},Ge=(0,n._)("h1",null,"Give Feedback",-1),Ke=(0,n._)("p",null,"Do you find Bill helpful? Something not working right? New feature request? You can submit it here.",-1),Le=(0,n._)("br",null,null,-1),Ne={class:"inputBox"},Je=(0,n._)("br",null,null,-1),Xe=(0,n._)("br",null,null,-1),es=["disabled"],ss={key:1,class:"spinner-border",role:"status"},is=(0,n._)("span",{class:"sr-only"},null,-1),ls=[is],as={key:1,class:"subscribe col-md-8"},ns=(0,n._)("h1",null,"Success",-1),ts=(0,n._)("p",null,"Thanks for your feedback!",-1),rs=[ns,ts],os={key:2,class:"subscribe col-md-8"},us=(0,n._)("h1",null,"Error",-1),cs=(0,n._)("p",null,"There was an issue saving your feedback, please try again later.",-1),ds=[us,cs];function ms(e,s,i,a,t,r){const o=(0,n.Q2)("validate");return(0,n.wg)(),(0,n.iD)("div",Pe,[(0,n._)("div",ze,[Me,t.isSuccess||t.isError?(0,n.kq)("",!0):((0,n.wg)(),(0,n.iD)("div",$e,[Ge,Ke,Le,(0,n._)("div",Ne,[(0,n.wy)((0,n._)("input",{type:"email",class:"form-control form-control-lg flex-grow-1 emailInput","onUpdate:modelValue":s[0]||(s[0]=e=>t.userEmail=e),placeholder:"Email (optional)"},null,512),[[o,"email"],[l.nr,t.userEmail]]),Je,(0,n.wy)((0,n._)("textarea",{"onUpdate:modelValue":s[1]||(s[1]=e=>t.feedback=e),autosize:"",placeholder:"Feedback",class:"form-control form-control-lg flex-grow-1"},null,512),[[l.nr,t.feedback]]),Xe,t.savingFeedback?(0,n.kq)("",!0):((0,n.wg)(),(0,n.iD)("button",{key:0,class:"btn btn-info ml-2",onClick:s[2]||(s[2]=(...e)=>r.submitFeedback&&r.submitFeedback(...e)),disabled:t.feedback.length<1},"Submit",8,es)),t.savingFeedback?((0,n.wg)(),(0,n.iD)("div",ss,ls)):(0,n.kq)("",!0)])])),t.isSuccess?((0,n.wg)(),(0,n.iD)("div",as,rs)):(0,n.kq)("",!0),t.isError?((0,n.wg)(),(0,n.iD)("div",os,ds)):(0,n.kq)("",!0)])])}var bs={name:"FeedbackComponent",data(){return{userEmail:"",feedback:"",isSuccess:!1,isError:!1,savingFeedback:!1}},methods:{async submitFeedback(){this.savingFeedback=!0,this.loadingQuery=!0,G.Z.post("/feedback",{email:this.userEmail,feedback:this.feedback}).then((()=>{this.isSuccess=!0,this.savingFeedback=!1})).catch((()=>{this.isError=!0,this.savingFeedback=!1}))}}};const hs=(0,w.Z)(bs,[["render",ms]]);var vs=hs;const ps={class:"container"},gs={class:"row"},fs=(0,n._)("div",{class:"headshot col-md-3"},[(0,n._)("img",{alt:"Vue logo",src:Q})],-1),ys={key:0,class:"spinner-border",role:"status"},ks=(0,n._)("span",{class:"sr-only"},null,-1),_s=[ks],ws={key:1,class:"subscribe col-md-8"},Es=(0,n._)("h1",null,"Success",-1),qs={key:2,class:"subscribe col-md-8"},Ss=(0,n._)("h1",null,"Error",-1),Ds=(0,n._)("p",null,"There was an issue verifying your email, please try again later.",-1),As=[Ss,Ds];function Qs(e,s,i,l,a,t){const r=(0,n.up)("router-link");return(0,n.wg)(),(0,n.iD)("div",ps,[(0,n._)("div",gs,[fs,a.savingEmail?((0,n.wg)(),(0,n.iD)("div",ys,_s)):(0,n.kq)("",!0),a.isSuccess?((0,n.wg)(),(0,n.iD)("div",ws,[Es,(0,n._)("p",null,[(0,n.Uk)("Your email has been verified, we'll send you periodic updates about Bill the AI. You can unsubscribe at any time "),(0,n.Wm)(r,{to:"/unsubscribe"},{default:(0,n.w5)((()=>[(0,n.Uk)("here")])),_:1}),(0,n.Uk)(".")])])):(0,n.kq)("",!0),a.isError?((0,n.wg)(),(0,n.iD)("div",qs,As)):(0,n.kq)("",!0)])])}var Us={name:"EmailVerificationComponent",mounted(){let e=(0,a.yj)(),s=e.params.id,i=e.params.email;G.Z.post("/verify-email",{id:s,email:i}).then((()=>{this.isSuccess=!0})).catch((()=>{this.isError=!0}))},data(){return{userEmail:"",isSuccess:!1,isError:!1,savingEmail:!1,errorMessage:""}}};const xs=(0,w.Z)(Us,[["render",Qs]]);var Cs=xs;const Bs={class:"container introComponent"},Fs=(0,n._)("div",{class:"row"},[(0,n._)("div",{class:"headshot col-md-3"},[(0,n._)("img",{alt:"Vue logo",src:Q})]),(0,n._)("div",{class:"intro col-md-8"},[(0,n._)("h1",null,"Ask Bill questions about various bills!"),(0,n._)("p",null,[(0,n.Uk)("Bill is the AI that reads the laws that congress passes and explains them to you. He's only read a few recent bills so far, but he's working on more. Select a bill from the menu, read through some of the questions, then ask Bill your own question. Here are some tips about how to ask Bill a good question: "),(0,n._)("ul",null,[(0,n._)("li",null,"Make your question specific for the best response, ask how the law effects a certain group of people, or a certain industry."),(0,n._)("li",null,'Bill knows all the text of the bills, but doesn\'t always remember the name of the law. Ask questions in terms of "the bill" instead.'),(0,n._)("li",null,"Read existing questions before asking your own, Bill sends his developer an invoice every month for all the questions he answers.")])])])],-1),Ts=[Fs];function js(e,s,i,l,a,t){return(0,n.wg)(),(0,n.iD)("div",Bs,Ts)}var Is={name:"IntroComponent"};const Os=(0,w.Z)(Is,[["render",js]]);var Vs=Os;i(2166);const Zs=(0,a.p7)({history:(0,a.r5)(),routes:[{path:"/home",component:Vs},{path:"/q_and_a/:bill_id",component:we},{path:"/signup",component:N},{path:"/unsubscribe",component:Re},{path:"/feedback",component:vs},{path:"/verify/:email/:id",component:Cs},{path:"/",redirect:"/home"}]});(0,l.ri)(A).use(Zs).mount("#app")}},s={};function i(l){var a=s[l];if(void 0!==a)return a.exports;var n=s[l]={exports:{}};return e[l].call(n.exports,n,n.exports,i),n.exports}i.m=e,function(){var e=[];i.O=function(s,l,a,n){if(!l){var t=1/0;for(c=0;c<e.length;c++){l=e[c][0],a=e[c][1],n=e[c][2];for(var r=!0,o=0;o<l.length;o++)(!1&n||t>=n)&&Object.keys(i.O).every((function(e){return i.O[e](l[o])}))?l.splice(o--,1):(r=!1,n<t&&(t=n));if(r){e.splice(c--,1);var u=a();void 0!==u&&(s=u)}}return s}n=n||0;for(var c=e.length;c>0&&e[c-1][2]>n;c--)e[c]=e[c-1];e[c]=[l,a,n]}}(),function(){i.n=function(e){var s=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(s,{a:s}),s}}(),function(){i.d=function(e,s){for(var l in s)i.o(s,l)&&!i.o(e,l)&&Object.defineProperty(e,l,{enumerable:!0,get:s[l]})}}(),function(){i.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){i.o=function(e,s){return Object.prototype.hasOwnProperty.call(e,s)}}(),function(){i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){i.p="/"}(),function(){var e={143:0};i.O.j=function(s){return 0===e[s]};var s=function(s,l){var a,n,t=l[0],r=l[1],o=l[2],u=0;if(t.some((function(s){return 0!==e[s]}))){for(a in r)i.o(r,a)&&(i.m[a]=r[a]);if(o)var c=o(i)}for(s&&s(l);u<t.length;u++)n=t[u],i.o(e,n)&&e[n]&&e[n][0](),e[n]=0;return i.O(c)},l=self["webpackChunkbill_the_ai"]=self["webpackChunkbill_the_ai"]||[];l.forEach(s.bind(null,0)),l.push=s.bind(null,l.push.bind(l))}();var l=i.O(void 0,[998],(function(){return i(7225)}));l=i.O(l)})();
//# sourceMappingURL=app.757763c3.js.map
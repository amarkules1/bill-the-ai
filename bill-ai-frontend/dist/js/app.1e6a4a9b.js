(function(){"use strict";var n={4172:function(n,e,t){var o=t(9242),s=t(3396),r=t.p+"img/logo.8a5253ec.png";const i=(0,s._)("div",{class:"header"},[(0,s._)("div",{class:"headshot"},[(0,s._)("img",{alt:"Vue logo",src:r})]),(0,s._)("div",{class:"intro"},[(0,s._)("h1",null,"Ask Bill a question about the Inflation Reduction Act"),(0,s._)("p",null,[(0,s.Uk)("Bill is the AI that reads the laws that congress passes and explains them to you. He's only read the Inflation Reduction Act so far, but he's working on more. Read through some of the questions bellow, then ask Bill your own question. Here are some tips about how to ask Bill a good question: "),(0,s._)("ul",null,[(0,s._)("li",null,"Make your question specific for the best response, ask how the law effects a certain group of people, or a certain industry."),(0,s._)("li",null,'Bill knows all the text of the Inflation Reduction Act, but doesn\'t always remember the name of the law. Ask questions in terms of "the bill" instead.'),(0,s._)("li",null,"Read existing questions before asking your own, Bill sends his developer an invoice every month for all the questions he answers.")])])])],-1),u=(0,s._)("br",null,null,-1);function l(n,e,t,o,r,l){const a=(0,s.up)("QuestionsAndAnswers");return(0,s.wg)(),(0,s.iD)(s.HY,null,[i,u,(0,s.Wm)(a)],64)}var a=t(7139);const c={class:"form-group d-flex queryBox"},d=["disabled"],f={key:1,class:"spinner-border",role:"status"},h=(0,s._)("span",{class:"sr-only"},null,-1),y=[h],p={key:0,class:"spinner-border",role:"status"},g=(0,s._)("span",{class:"sr-only"},null,-1),w=[g],b={key:1},v={class:"card-body"},m=(0,s._)("strong",null,"Question:",-1),k=(0,s._)("strong",null,"Answer:",-1);function A(n,e,t,r,i,u){return(0,s.wg)(),(0,s.iD)("div",null,[(0,s._)("div",c,[(0,s.wy)((0,s._)("input",{type:"text",class:"form-control form-control-lg flex-grow-1","onUpdate:modelValue":e[0]||(e[0]=n=>i.userQuery=n),placeholder:"Ask Bill a question about the Inflation Reduction Act"},null,512),[[o.nr,i.userQuery]]),i.loadingQuery?(0,s.kq)("",!0):((0,s.wg)(),(0,s.iD)("button",{key:0,class:"btn btn-primary ml-2",onClick:e[1]||(e[1]=(...n)=>u.submitQuery&&u.submitQuery(...n)),disabled:i.userQuery.length<20},"Submit",8,d)),i.loadingQuery?((0,s.wg)(),(0,s.iD)("div",f,y)):(0,s.kq)("",!0)]),i.loadingQuestions?((0,s.wg)(),(0,s.iD)("div",p,w)):(0,s.kq)("",!0),i.loadingQuestions?(0,s.kq)("",!0):((0,s.wg)(),(0,s.iD)("div",b,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(i.questionsAndAnswers,(n=>((0,s.wg)(),(0,s.iD)("div",{key:n.question,class:"card mb-3"},[(0,s._)("div",v,[(0,s._)("p",null,[m,(0,s.Uk)(" "+(0,a.zw)(n.question),1)]),(0,s._)("p",null,[k,(0,s.Uk)(" "+(0,a.zw)(n.answer),1)])])])))),128))]))])}var _={name:"QuestionsAndAnswers",data(){return{userQuery:"",queryResult:null,questionsAndAnswers:[],loadingQuery:!1,loadingQuestions:!0}},mounted(){this.fetchQuestionsAndAnswers()},methods:{async fetchQuestionsAndAnswers(){const n=await fetch("/ira-q-and-a");this.questionsAndAnswers=await n.json(),this.loadingQuestions=!1},async submitQuery(){this.loadingQuery=!0;const n=await fetch(`/ira-query?query=${this.userQuery}`);this.queryResult=await n.json(),this.questionsAndAnswers.unshift(this.queryResult),this.userQuery="",this.loadingQuery=!1}}},q=t(89);const Q=(0,q.Z)(_,[["render",A]]);var O=Q,x={name:"App",components:{QuestionsAndAnswers:O}};const j=(0,q.Z)(x,[["render",l]]);var R=j;t(2166);(0,o.ri)(R).mount("#app")}},e={};function t(o){var s=e[o];if(void 0!==s)return s.exports;var r=e[o]={exports:{}};return n[o].call(r.exports,r,r.exports,t),r.exports}t.m=n,function(){var n=[];t.O=function(e,o,s,r){if(!o){var i=1/0;for(c=0;c<n.length;c++){o=n[c][0],s=n[c][1],r=n[c][2];for(var u=!0,l=0;l<o.length;l++)(!1&r||i>=r)&&Object.keys(t.O).every((function(n){return t.O[n](o[l])}))?o.splice(l--,1):(u=!1,r<i&&(i=r));if(u){n.splice(c--,1);var a=s();void 0!==a&&(e=a)}}return e}r=r||0;for(var c=n.length;c>0&&n[c-1][2]>r;c--)n[c]=n[c-1];n[c]=[o,s,r]}}(),function(){t.n=function(n){var e=n&&n.__esModule?function(){return n["default"]}:function(){return n};return t.d(e,{a:e}),e}}(),function(){t.d=function(n,e){for(var o in e)t.o(e,o)&&!t.o(n,o)&&Object.defineProperty(n,o,{enumerable:!0,get:e[o]})}}(),function(){t.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(n){if("object"===typeof window)return window}}()}(),function(){t.o=function(n,e){return Object.prototype.hasOwnProperty.call(n,e)}}(),function(){t.r=function(n){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(n,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(n,"__esModule",{value:!0})}}(),function(){t.p="/"}(),function(){var n={143:0};t.O.j=function(e){return 0===n[e]};var e=function(e,o){var s,r,i=o[0],u=o[1],l=o[2],a=0;if(i.some((function(e){return 0!==n[e]}))){for(s in u)t.o(u,s)&&(t.m[s]=u[s]);if(l)var c=l(t)}for(e&&e(o);a<i.length;a++)r=i[a],t.o(n,r)&&n[r]&&n[r][0](),n[r]=0;return t.O(c)},o=self["webpackChunkbill_ai_frontend"]=self["webpackChunkbill_ai_frontend"]||[];o.forEach(e.bind(null,0)),o.push=e.bind(null,o.push.bind(o))}();var o=t.O(void 0,[998],(function(){return t(4172)}));o=t.O(o)})();
//# sourceMappingURL=app.1e6a4a9b.js.map
<template>
    <div class="card-body">
        <p><strong>Question:</strong> {{ q.question }}</p>
        <p><strong>Answer:</strong> {{ q.answer }}</p>
    </div>
</template>
<script>
export default {
    name: 'QuestionComponent',
    props: {
        q: Object
    }
}
</script>
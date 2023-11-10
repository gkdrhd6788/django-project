<template>
    <div>
        <form @click.prevent="inputKeyword">
            <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="검색어를 입력해주세요."
            v-model="keyword">
            <button class="btn btn-outline-secondary" >검색</button>
        </div>
        </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'
const keyword = ref('')
const emit = defineEmits()

const inputKeyword = function(event){ //event안써도 되나??
    console.log(keyword.value)
    emit('inputKeyword',keyword.value)
}

</script>

<style scoped>

</style>
<template>
    <div class="card">
        <img class="card__image" :src="icon">
        <div class="card__content">
            <slot/>
        </div>
        <div class="card__tools">
            <img :src="require('@/assets/edit.png')" @click="$emit('edited')" v-if="editable">
            <img :src="require('@/assets/remove.png')" @click="$emit('deleted')">
        </div>
    </div>
</template>

<script>
export default {
    props: {
        icon: String,
        editable: Boolean,
    }
}
</script>

<style>
.card {
    display: flex;
    align-items: center;
    padding: 15px 0;
    width: 100%;
}

.card__image {
    width: 50px;
    height: 50px;
    border-radius: 10px;
}

.card__content {
    margin-left: 30px;
    font-size: 1.2em;
}

.card__tools {
    margin-left: auto;
}

.card__tools > img {
    width: 20px;
    height: 20px;
    margin-left: 4px;
}

.card + .card {
    border-top: 1px solid #cdcdcd;
}
</style>
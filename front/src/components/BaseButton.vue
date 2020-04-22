<template>
  <button class="button" @click="$emit('click')">
      <slot></slot>
  </button>
</template>

<script>
export default {

}
</script>

<style>
    .button {
        border-radius: 10px;
        background-color: #F84E55;
        color: #ffffff;
        min-width: 184px;
        height: 40px;
        border: none;
    }



    button::-moz-focus-inner {
        border: 0;
    }

    a {
        outline: 0;
    }
</style>
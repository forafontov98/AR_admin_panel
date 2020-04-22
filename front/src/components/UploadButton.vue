<template>
<div class="download-button">
  <span class="download-button__button" @click="$refs.input.click()">Загрузить</span>
  <input type="file" ref="input" @change="uploadFile" hidden>
</div>
</template>

<script>
import API from "@/api";

export default {
  methods: {
    async uploadFile() {
      const file = this.$refs.input.files[0];

      this.$emit('file-uploaded', await API.uploadFile(file));
    }
  }
}
</script>

<style>
.download-button {
  margin: 10px 0;
}

.download-button__button {
    margin: 5px 0;
    color: #F84E55;
    cursor: pointer;
}
</style>
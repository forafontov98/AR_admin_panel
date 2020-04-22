<template>
  <div>
    <base-button @click="$refs.input.click()">Добавить текстуру</base-button>
    <input type="file" ref="input" @change="createTexture" hidden>
    <base-card
      v-for="card in cards"
      :key="card.id"
      :icon="card.file.file"
      @updated="$router.go(`/objects/${card.id}`)"
      @deleted="deleteObject(card.id)"
    >{{ card.file.file.split('/').slice(-1)[0] }}</base-card>
  </div>
</template>

<script>
import API from "@/api";
import BaseButton from "@/components/BaseButton";
import BaseCard from "@/components/BaseCard";

export default {
  components: { BaseButton, BaseCard },
  async mounted() {
    this.cards = await API.listTextures();
  },
  data() {
    return {
      cards: []
    };
  },
  methods: {
      async createTexture() {
          const file_id = (await API.uploadFile(this.$refs.input.files[0])).id;
          await API.createTexture(file_id);
          this.cards = await API.listTextures();
      },
      deleteObject(id) {
          API.deleteTexture(id);
          this.cards = this.cards.filter(c => c.id !== id);
      }
  }
};
</script>

<style>
</style>
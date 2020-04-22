<template>
  <div>
    <base-button @click="$router.push('/objects/new')">Добавить объект</base-button>
    <base-card
      v-for="card in cards"
      :key="card.id"
      :icon="card.preview.file"
      editable
      @edited="$router.push(`/objects/${card.id}`)"
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
    this.cards = await API.listObjects();
  },
  data() {
    return {
      cards: []
    };
  },
  methods: {
      deleteObject(id) {
          API.deleteObject(id);
          this.cards = this.cards.filter(c => c.id !== id);
      }
  }
};
</script>

<style>
</style>
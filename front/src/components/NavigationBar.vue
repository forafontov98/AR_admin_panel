<template>
  <nav
    :class="{'navigation--hidden': hidden}"
    class="navigation"
  >
        <router-link class="navigation__link" to="/objects">Объекты</router-link>
        <router-link class="navigation__link" to="/textures">Текстуры</router-link>
        <router-link class="navigation__link navigation__link--tool" to="/login">Выйти</router-link>
  </nav>
</template>

<script>
export default {
    props: {
        hidden: Boolean,
    }
}
</script>

<style>
.navigation {
    display: flex;
    flex-direction: row;
    justify-content: start;
    align-content: center;
    background-color: white;
    height: 60px;
    padding: 0 25px;
    border-radius: 0 0 25px 25px;
}

.navigation--hidden {
    visibility: hidden;
}

.navigation__link {
    display: flex;
    align-items: center;
    margin-right: 25px;
    text-decoration: none;
    color: #8d8d8d;
}

.router-link-active {
    color: #000000;
    font-weight: bold;
}

.navigation__link--tool {
    margin-left: auto;
    color: #F84E55;
    font-weight: bold;
}
</style>
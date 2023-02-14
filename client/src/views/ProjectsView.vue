<template>

  <MainSection/>


</template>

<script>
import MainSection from "@/components/projectsPage/MainSection.vue";


export default {
  name: "ProjectsView",
  components: {
    MainSection,
  }
}
</script>

<style scoped>

  footer {
    margin-top: 100vh;
  }

 .navbar07_component{
    background-color: transparent;
    backdrop-filter: blur(4px) brightness(50%);
  }
</style>
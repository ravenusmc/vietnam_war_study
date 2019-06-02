<template>
  <div>

    <header>
      <div>
        <h1 class='title_header'>Vietnam</h1>
      </div>
      <!-- <img src='@/assets/img/rice_fields.jpg'> -->
    </header>

  </div>
</template>

<script>
export default {
  name: 'Header',
}
</script>

<style scoped>

header {
  background-image: url('../../assets/img/rice_fields.jpg');
  width: 100%;
  height: 500px;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

img {
  width: 100%;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}

.title_header {
  font-size: 12rem;
  font-weight: 600;
  letter-spacing: -.3rem;
  color: #fff;
}

</style>

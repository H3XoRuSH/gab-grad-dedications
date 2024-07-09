<template>
  <img class="logo" src="@/assets/gab.gif" height="420" />
  <div class="greetings">
    <h1 class="colored">Hi there! I am Gab.</h1>
    <h3>Type your code below to see my message for you!</h3>
    <form>
      <input type="text" />
    </form>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}

input {
  display: block;
  margin-top: 10px;
  padding: 2px;
}

.logo {
  margin-bottom: 1em;
}
</style>

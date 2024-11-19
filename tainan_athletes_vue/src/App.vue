<template>
  <div id="app">
    <nav>    </nav>
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body {
  background-color: #1a2b47;
	margin: 0;
}

// nav {
//   padding: 30px;

//   a {
//     font-weight: bold;
//     color: #ffffff;

//     &.router-link-exact-active {
//       color: #43d895;
//     }
//   };

//   background-color: #1a2b47;
// }
</style>

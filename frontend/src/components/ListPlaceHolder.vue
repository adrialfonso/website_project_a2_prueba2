<template>
  <div class="options-content">
    <!-- Placeholder Content for Grid -->
    <div class="card-book-placeholder" v-for="index in items" :key="index">
      <div class="image-wrap-placeholder">
        <div class="image-placeholder"></div>
      </div>
      <div class="text-wrap">
        <div class="genres-placeholder"> </div>
        <div class="text-card-placeholder"></div>
        <div class="author-placeholder"></div>
        <div class="synopsis-placeholder"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ListTabPlaceholder',
  props: {
    items: Number
  }
}
</script>

<style scoped>
.options-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.card-book-placeholder {
  display: flex;
  gap: var(--panel-gap);
  flex-direction: row;
  padding-bottom: var(--panel-gap);
}

.image-wrap-placeholder{
  order: 1;
  align-content: center;
  align-items: center;
}

.image-placeholder {
  height: 11rem;
  width: 7rem;
  background: linear-gradient(to right, #eee 2%, #ddd 18%, #eee 33%);
  background-size: 200% 100%;
  animation: placeholderAnimate 3s infinite linear forwards;
  border-radius: var(--border-radius);
}

.text-wrap {
  order: 2;
  padding: calc(var(--panel-gap));
  margin-left: calc(var(--panel-gap) *3);
  display: grid;
  grid-template-areas: 'genres'
                        'title'
                       'author'
                       'synopsis';
  grid-template-rows: 1fr 1fr 1fr auto;
  align-content: center;
  color: var(--text-color);
  width: 100%;
  gap: calc(var(--panel-gap) *-1);
  align-items: start;
  height: 12rem;
}

.genres-placeholder{
  grid-area: genres;
  display: flex;
  margin-bottom: calc(var(--panel-gap) /2);
  width: 25%;
  height: 1.25rem;
  background: linear-gradient(to right, #eee 2%, #ddd 18%, #eee 33%);
  background-size: 200% 100%;
  animation: placeholderAnimate 3s infinite linear;
  border-radius: var(--border-radius);
}

.text-card-placeholder {
  grid-area: title;
  width: 100%;
  height: 5rem;
  background: linear-gradient(to right, #eee 2%, #ddd 18%, #eee 33%);
  background-size: 200% 100%;
  animation: placeholderAnimate 3s infinite linear;
  border-radius: var(--border-radius);
}

.author-placeholder{
  grid-area: synopsis;
  width: 10%;
  height: 1.25rem;
  align-self: start;
  background: linear-gradient(to right, #eee 2%, #ddd 18%, #eee 33%);
  background-size: 200% 100%;
  animation: placeholderAnimate 3s infinite linear;
  border-radius: var(--border-radius);
}

synopsis-placeholder{
  grid-area: synopsis;
  align-self: start;
  width: 100%;
  height: 5rem;
  background: linear-gradient(to right, #eee 2%, #ddd 18%, #eee 33%);
  background-size: 200% 100%;
  animation: placeholderAnimate 3s infinite linear;
  border-radius: var(--border-radius);
}

@keyframes placeholderAnimate {
  0% {
    background-position: -650px 0;
  }
  100% {
    background-position: 650px 0;
  }
}
</style>

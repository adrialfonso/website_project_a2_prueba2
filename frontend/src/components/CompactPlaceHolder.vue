<template>
  <div class="options-content">
    <!-- Placeholder Content for Grid -->
    <div class="card-book-placeholder" v-for="index in items" :key="index">
      <div class="left-placeholder" />
      <div class="right-placeholder" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'CompactTabPlaceholder',
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
  justify-content: space-between;
  gap: calc(var(--panel-gap) * 2);
  align-items: center;
}

.left-placeholder{
  width: 20%;
  flex: 1;
  margin-right: 1rem;
  height: 1.25rem;
  background: linear-gradient(to right, #eee 2%, #ddd 18%, #eee 33%);
  background-size: 200% 100%;
  animation: placeholderAnimate 3s infinite linear forwards;
  border-radius: var(--border-radius);
}

.right-placeholder{
  width: 20%;
  height: 1.25rem;
  background: linear-gradient(to right, #eee 2%, #ddd 18%, #eee 33%);
  background-size: 200% 100%;
  animation: placeholderAnimate 3s infinite linear forwards;
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

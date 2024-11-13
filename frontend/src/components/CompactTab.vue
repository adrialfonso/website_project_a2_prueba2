<template>
  <div class="options-content">

    <div class="header-compact">
      <div class="left">
        Book's name
      </div>
      <div class="right">
        Author's name
      </div>
    </div>

    <div class="line"/>

    <div v-for="(item, index) in column" :key="index" v-if="item.data" class="btn card-book-wrap" @click="startSearch(item)">
          <h5 class="book-name left">
            {{ item.data.title }}
          </h5>
          <h4 class="author-name right">
            {{ item.data.authors }}
          </h4>
    </div>

  </div>
</template>

<script>
export default {
  name: 'CompactTab',
  props: {
    column: Array
  },
  methods: {
    startSearch (item) {
      if ((!this.$route.query.search || this.$route.query.search !== item.data.title) ||
        (!this.$route.query.type || this.$route.query.type !== item.type)) {
        const currentQuery = { ...this.$route.query }

        delete currentQuery.category
        delete currentQuery.search
        delete currentQuery.type

        const newQuery = {
          ...currentQuery,
          search: item.data.title,
          type: item.type
        }

        this.$router.push({ query: newQuery }).catch(err => {
          if (err.name !== 'NavigationDuplicated') {
            console.error('Error replacing the route', err)
          }
        })
      }
    }
  }
}
</script>

<style scoped>

.options-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.btn {
  border: 0;
  padding: var(--panel-gap);
  border-radius: var(--border-radius);
  color: var(--text-color);

}

.btn:hover {
  background: var(--half-transparent-background);
}

.header-compact, .card-book-wrap{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--panel-gap);
}

.title-header-compact {
  font-weight: 600;
  font-size: var(--font-size-xs);
}

.left {
  text-align: left;
}

.right {
  text-align: right;
}

.line {
  height: 1px;
  background: var(--gray-background);
  box-sizing: border-box;
  margin-top: calc(var(--panel-gap) * -1);
  margin-inline: var(--panel-gap);
}

.book-name{
    text-transform: uppercase;
}

.book-name, .author-name{
  font-size: var(--font-size-xs);
  font-weight: 600;
}

</style>

<template>
  <div class="options-content" :class="{'options-content-fit': column.length > 1}">
        <div v-for="(item, index) in column" :key="index" v-if="item.data" class="btn" @click="startSearch(item)">
          <div class="card-book">
            <img loading="lazy"  src="@/assets/cover.png" class="image" alt="Cover Book">
            <div class="text-wrap">
              <h5 class="text-card">
                {{ item.data.title }}
              </h5>
            </div>
          </div>
        </div>
  </div>
</template>

<script>
export default {
  name: 'GridTab',
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
.options-content{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(10rem, 1fr));
  gap: 1rem;
  align-items: center;
  padding-block: var(--panel-gap);
}

.options-content-fit{
 grid-template-columns: repeat(auto-fit, minmax(10rem, 1fr));
}

.btn{
  padding: var(--panel-gap);
  border: 0;
  border-radius: var(--border-radius);
}

.btn:hover{
  background: var(--half-transparent-background);
}

.card-book{
  color: var(--text-color);
  display: flex;
  flex-direction: column;
  gap: var(--panel-gap);
}

.card-book.list{
  flex-direction: row;
}

.image{
  border-radius: var(--border-radius);
  box-shadow: 0 0 0.5rem var(--half-transparent-main-background);
}

.text-wrap{
  justify-content: center;
  display: flex;
}

.text-card{
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: var(--font-size-xs);
}

</style>

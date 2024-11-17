<template>
  <div class="options-content">
        <div v-for="(item, index) in column" :key="index" v-if="item.data" class="btn" @click="startSearch(item)">
          <div class="card-book" >
            <div class="image-wrap">
              <img loading="lazy" src="@/assets/cover.png" class="image" alt="Cover Book">
            </div>
            <div class="text-wrap">
              <div class="genres">
                <a v-for="genre in item.data.genres" :key="genre">
                  {{ genre }}
                </a>
              </div>
              <h4 class="text-card">
                {{ item.data.title }}
              </h4>
              <h5 class="author">
                By {{ item.data.authors }}
              </h5>
              <p class="synopsis">
                {{ item.data.synopsis }}
              </p>
            </div>
          </div>
        </div>
  </div>
</template>

<script>
export default {
  name: 'ListTab',
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
.btn{
  border: 0;
}

.btn{
  padding: var(--panel-gap);
  border: 0;
  border-radius: var(--border-radius);
}

.btn:hover{
  background: var(--half-transparent-background);
}

.options-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.card-book {
  display: flex;
  gap: var(--panel-gap);
  flex-direction: row;
  padding-bottom: var(--panel-gap);
}

.image-wrap{
  order: 1;
  width: 25%;
  align-content: center;
  align-items: center;
}

.image {
  width: 9.375rem;
  height: 11rem;
  border-radius: var(--border-radius);
  box-shadow: 0 0 0.5rem var(--half-transparent-main-background);
}

.text-wrap{
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
  align-items: center;
  color: var(--text-color);
  width: 100%;
}

.genres{
  grid-area: genres;
  display: flex;
  color: var(--second-text-color);
  line-height: 1rem;
  font-size: var(--font-size-xs);
  gap: var(--panel-gap);
  margin-bottom: calc(var(--panel-gap) /2);
  font-weight: 700;
}

.text-card{
  grid-area: title;
  display: flex;
  font-size: var(--font-size-medium);
  font-weight: 700;
}

.author{
  grid-area: author;
  display: flex;
  font-style: italic;
  font-weight: 700;
  font-size: var(--font-size-xs);
}

.synopsis{
  grid-area: synopsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: var(--font-size-xs);
  text-align: left;
}
</style>

<template>
  <div>
    <div id="page" class="grid-layout min-vh-100">
      <main-header
        :actualPage="currentTab"
        @category-selected="startCategory"
        @home-update="startHome"
        @search-selected="startSearch"
      />
      <div class="tabs">
        <div class="view-as gradient-custom-header">
          <footer-tabs />
        </div>
        <div class="not-found-container">
          <img src="@/assets/not-found.png" alt="Page Not Found" class="not-found-image" />
          <h1>404</h1>
          <p>Oops! The page you are looking for does not exist.</p>
          <router-link to="/">
            <button class="btn btn-home">Go Back Home</button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
const PageEnum = Object.freeze({
  HOME: 'default',
  SEARCH: 'book-page',
  CATEGORY: 'category',
  PROFILE: 'Profile',
  NOTFOUND: 'not-found'
})
export default {
  name: 'NotFoundPage',
  components: {
    'main-header': Navbar,
    'footer-tabs': Footer
  },
  data () {
    return {
      currentTab: 'not-found'
    }
  },
  methods: {
    startHome () {
      this.currentTab = PageEnum.HOME
      this.initializeSearchResults()
    },
    startCategory (data) {
      if (this.currentTab !== PageEnum.CATEGORY) {
        if (this.searchResults.length === 1) {
          this.initializeSearchResults()
        }
        this.currentTab = PageEnum.CATEGORY
        const newSearch = this.searchResults.find(column => column.title === data[0])
        if (newSearch) {
          this.searchResults = [newSearch]
        }
      }
    },
    startSearch (data) {
      this.currentTab = PageEnum.SEARCH
      console.log('Searching for:', data)

      // If a request is made to the API, it should be async
      // Ejemplo de Book
      if (data[1] === 'book') {
        this.searchResults = [
          {
            title: 'Search',
            list:
              {
                type: 'book',
                data: {
                  title: 'Book1',
                  Authors: 'AuthorsName',
                  Synopsis: 'Synopsis info',
                  BuyLink: 'BuyLink info',
                  Genres: 'Gerne1, Gernre2',
                  Rating: 0.0,
                  Editorial: 'EditorialName',
                  Comments: [],
                  PublicationDate: '11/11/11',
                  Image: 'image'
                }
              }
          }
        ]
      } else if (data[1] === 'user') {
        // Ejemplo de user
        this.searchResults = [
          {
            title: 'Search',
            list:
              {
                type: 'user',
                data: {
                  name: 'Book1',
                  surname: 'AuthorsName',
                  username: 'Synopsis info',
                  email: 'BuyLink info'
                }
              }
          }
        ]
      }
    }
  }
}
</script>

<style scoped>
.view-as {
  grid-area: filter-option;
  display: flex;
  flex-direction: row;
  position: sticky;
  top: 0;
  opacity: 1;
  justify-content: flex-start;
  padding: calc(var(--panel-gap) * 2);
  align-items: center;
}

.not-found-image {
  max-width: 150px;
  height: auto;
  margin-bottom: var(--panel-gap);
}

.btn-home:hover {
  transform: scale(1.05);
}
.not-found-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 100%;
  padding: var(--panel-gap);
}
.btn-home{
  margin-right: var(--panel-gap);
  margin-top: var(--panel-gap);
  font-weight: 700;
  color: var(--text-color);
  width: 9rem;
  height: 3rem;
  transition: transform 0.3s ease-in-out;
  border-radius: calc(var(--border-radius) * 2);
  background: var(--purple-background);
}
.tabs {
  background: var(--box-background-color);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: calc(var(--border-radius) * 2);
  overflow: auto;
  grid-area: tabs;
  margin-left: calc(-1 * var(--panel-gap));
  display: grid;
  gap: var(--panel-gap);
  grid-template-areas: 'filter-option'
                       'main-page'
                       'footer';
  grid-template-rows: auto 1fr auto;
  max-height: 100vh;
  color: var(--text-color);
  align-content: center;
}
.grid-layout {
  display: grid;
  gap: var(--panel-gap);
  grid-template-areas:
    'global-nav global-nav global-nav'
    'left-slider tabs tabs';
  grid-template-rows: auto 1fr;
  grid-template-columns: 0 auto 0;
  padding: var(--panel-gap);
  padding-top: 0;
  background-color: var(--main-background);
}
h1 {
  font-size: 3rem;
}

p {
  font-size: 1.5rem;
}
</style>

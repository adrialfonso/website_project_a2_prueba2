<template>
  <div class="suggestions" v-if="hasSuggestions">
    <suggestion
      v-for="(category, index) in categories"
      :key="category.title"
      v-if="category.suggestions.length"
      :suggestions="category.suggestions"
      :title="category.title"
      :icon="category.icon"
      :isNext="index < categories.length - 1 ? categories[index + 1].suggestions.length > 0 : false"
      :selectSuggestionAvailable="category.title !== 'Error'"
      :selectSuggestion="selectSuggestion"
      @select="selectSuggestion"/>
  </div>
</template>

<script>
import Suggestion from '@/components/Suggestion'

export default {
  name: 'Suggestions',
  components: {'suggestion': Suggestion},
  props: {
    filteredSuggestionsUsers: Array,
    filteredSuggestionsBooks: Array,
    errorMessages: Array,
    inputClear: Boolean
  },
  computed: {
    hasSuggestions () {
      return (
        this.filteredSuggestionsUsers.length > 0 ||
        this.filteredSuggestionsBooks.length > 0 ||
        this.errorMessages.length > 0
      )
    },
    categories () {
      return [
        {
          title: 'Users',
          suggestions: this.filteredSuggestionsUsers,
          icon: this.userIcon
        },
        {
          title: 'Books',
          suggestions: this.filteredSuggestionsBooks,
          icon: this.bookIcon
        },
        {
          title: 'Error',
          suggestions: this.errorMessages,
          icon: this.errorIcon
        }
      ]
    },
    userIcon () {
      return `
    <svg width="16" height="16" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M34 34C34 31.8783 33.1571 29.8434 31.6569 28.3431C30.1566 26.8429 28.1217 26 26 26H10C7.87827 26 5.84344 26.8429 4.34315 28.3431C2.84285 29.8434 2 31.8783 2 34H34Z" fill="white"/>
                                    <path d="M18 18C22.4183 18 26 14.4183 26 10C26 5.58172 22.4183 2 18 2C13.5817 2 10 5.58172 10 10C10 14.4183 13.5817 18 18 18Z" fill="white"/>
                                    <path d="M34 34C34 31.8783 33.1571 29.8434 31.6569 28.3431C30.1566 26.8429 28.1217 26 26 26H10C7.87827 26 5.84344 26.8429 4.34315 28.3431C2.84285 29.8434 2 31.8783 2 34H34Z" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M18 18C22.4183 18 26 14.4183 26 10C26 5.58172 22.4183 2 18 2C13.5817 2 10 5.58172 10 10C10 14.4183 13.5817 18 18 18Z" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                                  </svg>
    `
    },
    bookIcon () {
      return `<svg width="16" height="16" viewBox="0 0 36 44" fill="none" xmlns="http://www.w3.org/2000/svg">
                                  <path d="M2 37C2 35.6739 2.52678 34.4021 3.46447 33.4645C4.40215 32.5268 5.67392 32 7 32H34" fill="white"/>
                                  <path d="M7 2H34V42H7C5.67392 42 4.40215 41.4732 3.46447 40.5355C2.52678 39.5979 2 38.3261 2 37V7C2 5.67392 2.52678 4.40215 3.46447 3.46447C4.40215 2.52678 5.67392 2 7 2Z" fill="white"/>
                                  <path d="M2 37C2 35.6739 2.52678 34.4021 3.46447 33.4645C4.40215 32.5268 5.67392 32 7 32H34M2 37C2 38.3261 2.52678 39.5979 3.46447 40.5355C4.40215 41.4732 5.67392 42 7 42H34V2H7C5.67392 2 4.40215 2.52678 3.46447 3.46447C2.52678 4.40215 2 5.67392 2 7V37Z" stroke="#282828" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                                  </svg>`
    },
    errorIcon () {
      return `<svg width="17" height="17" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10 15C10.2833 15 10.5208 14.9042 10.7125 14.7125C10.9042 14.5208 11 14.2833 11 14C11 13.7167 10.9042 13.4792 10.7125 13.2875C10.5208 13.0958 10.2833 13 10 13C9.71667 13 9.47917 13.0958 9.2875 13.2875C9.09583 13.4792 9 13.7167 9 14C9 14.2833 9.09583 14.5208 9.2875 14.7125C9.47917 14.9042 9.71667 15 10 15ZM9 11H11V5H9V11ZM10 20C8.61667 20 7.31667 19.7375 6.1 19.2125C4.88333 18.6875 3.825 17.975 2.925 17.075C2.025 16.175 1.3125 15.1167 0.7875 13.9C0.2625 12.6833 0 11.3833 0 10C0 8.61667 0.2625 7.31667 0.7875 6.1C1.3125 4.88333 2.025 3.825 2.925 2.925C3.825 2.025 4.88333 1.3125 6.1 0.7875C7.31667 0.2625 8.61667 0 10 0C11.3833 0 12.6833 0.2625 13.9 0.7875C15.1167 1.3125 16.175 2.025 17.075 2.925C17.975 3.825 18.6875 4.88333 19.2125 6.1C19.7375 7.31667 20 8.61667 20 10C20 11.3833 19.7375 12.6833 19.2125 13.9C18.6875 15.1167 17.975 16.175 17.075 17.075C16.175 17.975 15.1167 18.6875 13.9 19.2125C12.6833 19.7375 11.3833 20 10 20Z" fill="white"/>
                </svg>
                `
    }
  },
  methods: {
    selectSuggestion (suggestion, type) {
      // Emit the selected suggestion to the parent component
      this.$emit('suggestion-selected', [suggestion, type])
    }
  }
}
</script>

<style scoped>
.suggestions {
  position: absolute;
  background: var(--box-background-color);
  border: 1px solid var(--half-transparent-background);
  border-radius: calc(var(--border-radius) * 2);
  z-index: 5;
  overflow-y: auto;
  height: auto;
  width: 100%;
  margin-top: 0.5rem;
  max-height: 100vh;
}
</style>

<template>
  <div class="view-as gradient-custom-header">

      <!-- Toogle View: Grid, List and Compact -->
      <div class="toggle-wrap" v-if="currentTab !== 'book-page'">
        <input type="radio" id="toggle1" name="toggle" class="toggleCheckbox" @click="setView('grid')" :checked="view === 'grid'"/>
        <input type="radio" id="toggle2" name="toggle" class="toggleCheckbox" @click="setView('list')" :checked="view === 'list'"/>
        <input type="radio" id="toggle3" name="toggle" class="toggleCheckbox" @click="setView('compact')" :checked="view === 'compact'"/>

        <div class="toggleContainer">
          <label for="toggle1" class="toggleLabel">
            <svg width="16" height="16" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
              <title>Grid View</title>
              <path d="M20 6H6V20H20V6Z" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M42 6H28V20H42V6Z" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M42 28H28V42H42V28Z" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M20 28H6V42H20V28Z" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </label>

          <label for="toggle2" class="toggleLabel">
            <svg width="16" height="16" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
              <title>List View</title>
              <path d="M38 9.5H24M38 31H24M2 2H16V16H2V2ZM2 24H16V38H2V24Z" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </label>

          <label for="toggle3" class="toggleLabel centered">
            <svg width="16" height="16" viewBox="0 0 40 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <title>Compact View</title>
              <path d="M28.5 9H2M38 2.5H2M38 24H2M2 17H21" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </label>

          <div class="toggleIndicator gradient-custom"></div>
        </div>

      </div>
    </div>
</template>
<script>

export default {
  name: 'FilterHeader',
  props: {
    searchResults: Array,
    currentTab: String
  },
  computed: {
    view () {
      return this.$store.getters.displayMode
    },
    username () {
      return this.$store.getters.username
    }
  },
  methods: {
    setView (display) {
      if (display !== this.view) {
        this.$store.dispatch('setDisplayMode', display)
      }
    }
  }
}
</script>
<style scoped>
.view-as{
  grid-area: filter-option;
  display: flex;
  flex-direction: row;
  position: sticky;
  top: 0;
  opacity: 1;
  justify-content:flex-start;
  padding: calc(var(--panel-gap)*2);
  align-items: center;
}

.toggle-wrap {
    display: flex;
    align-items: center;
    margin-left: auto;
    padding: calc(var(--panel-gap) / 2);
}

.toggleContainer {
    position: relative;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border: 1px solid var(--box-border-color);
    border-radius: calc(var(--border-radius) * 2);
    background: var(--box-background-color);
    font-weight: bold;
    overflow: hidden;
    align-items: center;
}

.toggleLabel {
    padding: 10px;
    text-align: center;
    cursor: pointer;
    color: var(--text-color);
    font-size: var(--font-size-xs);
    z-index: 1;
    transition: color 0.3s;
    display: flex;
}

.toggleIndicator {
    content: '';
    position: absolute;
    width: 29.33%;
    height: 90%;
    left: 0;
    border-radius: calc(var(--border-radius) * 2);
    transition: all 0.3s;
}

.toggleCheckbox {
    display: none;
}

#toggle1:checked ~ .toggleContainer  .toggleIndicator {
    left: 2%;
}

#toggle2:checked ~ .toggleContainer .toggleIndicator {
    left: 35.33%;
}

#toggle3:checked ~ .toggleContainer .toggleIndicator {
    left: 68.66%;
}
</style>

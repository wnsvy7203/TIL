# Vuex

## Problem

- Vue CLI 및 Vuex를 활용하여 todo 앱을 완성하기 전 사전작업을 진행하고자 한다. 프로젝트를 생성 후 필요한 컴포넌트들을 생성하고 다음 워크샵을 위해 어떻게 구조화 할 것인지 계획하시오.

```vue
App 하위 컴포넌트로 TodoList, TodoForm 생성 및 등록
TodoList 하위 컴포넌트로 TodoListItem 생성 및 등록

// App.vue
<template>
  <div>
    <TodoList/>
    <TodoForm/>
  </div>
</template>    

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
}
</script>

// TodoList.vue
<template>
  <div>
    <TodoListItem/>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'App',
  components: {
    TodoListItem,
  },
}
</script>
```




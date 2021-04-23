<template>
    <div class="dashboard">
      <Header />
    </div>
    <main>
      <Toolbar />
      <Team />
    </main>
</template>

<script>
import Header from '@/components/Header'
import Toolbar from '@/components/Toolbar'
import Team from '@/components/Team'
export default {
  name: 'App',
  components: {
    Header,
    Toolbar,
    Team,
  
  }
}
</script>

<style>
:root{
  --primary:#611F69;
  --primary-alt:#a561aa;
  --light:#f7fcfe;
  --light-alt:#F8F8F8;
  --grey:#777474;
  --dark:#131A26;
}

*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family:"Fira sans", sans-serif;
}
body {
  background-color: var(--light);
}
main{
  width: 100vw;
  overflow: hidden;
}
input, button{
  appearance: none;
  outline: none;
  border: none;
  background: none;
}

.button{
  display: inline-block;
  padding: 8px 16px;
  background-color: var(--primary);
  color: #fff;
  font-size: 20px;
  font-weight: 700;
  text-transform: uppercase;
  cursor: pointer;
  border-radius: 6px;
  transition: 0.4s;
}
.button:hover{
  background-color: var(--primary-alt);
}
.button.button-outline{
  background-color: transparent;
  border: 2px solid var(--primary);
  padding: 6px 14px;
  color: var(--primary);
}
.button.button-outline:hover{
  color: #fff;
  background-color: var(--primary);
}

.button.button-small{
  padding: 4px 8px;
  font-size: 18px;
  font-weight: 600;
  
}
.button.button-alert{
  background-color: crimson;
  
}
.button-group{
  display: flex;
  margin: 0 -8px;
  
}
.button-group.group-end{
  justify-content: flex-end;
}
.button-group.button{
  margin: 0 8px;
}
</style>

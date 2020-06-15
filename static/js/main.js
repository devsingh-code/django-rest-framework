const root = document.getElementById('root');


document.querySelector('#postForm').addEventListener('submit',e => {
  e.preventDefault();
  const title = document.getElementById('title');
  const content = document.getElementById('content');
  const author = document.getElementById('author');
  createPost(title.value, content.value, author.value);
  title.value = '';
  content.value ='';
  author.value ='';
})


function createPost(title, content, author){
  const data = {
    method: 'POST',
    headers: {
      'content-type':"application/json"
    },
    body:JSON.stringify({
      title,content,author
    })

  }
  fetch('api/posts/create/',data)
  .then(()=>{
    getPostList();
  } )
  .catch(err =>{
    console.log(err);
  } )
}


function getPostList(){
  fetch('/api/posts/')
  .then(res => res.json())
  .then(data =>{
    clearChildren(root);
    renderPosts(data);
  })
  .catch(err =>{
    console.log(err);
  })
}

function renderPosts(data){
  return data.map(
    post => {
      renderPost(post);
    })
}

function createNode(element){
  return document.createElement(element);
}

function append(parent, el){
  return parent.appendChild(el);
}

function clearChildren(node){
  while (node.firstChild){
    node.removeChild(node.firstChild);
  }
}

function renderPost(post){

  const div =createNode('div');
  div.className = 'post-item';
  const title = createNode('h2');
  const link =createNode('a');
  link.href = `/posts/${post.id}/`;
  append(link, title);


  const content = createNode('p');
  const publishDate = createNode('span');
  const lastUpdated = createNode('span');
  const author = createNode('small');

  author.innerText = post.author;
  title.innerText = `${post.title} written by ${post.author}`;

  content.innerText = post.content;
  publishDate.innerText = `Published :${new Date(post.publish_date).toUTCString()}`;
  lastUpdated.innerText = `Last Updated :${new Date(post.updated).toUTCString()}`;

  append(div,link);
  append(div,content);
  append(div,publishDate);
  append(div,lastUpdated);
  append(root,div);

}

getPostList()

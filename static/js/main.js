
document.querySelector('#postForm').addEventListener('submit',e => {
  e.preventDefault();
  console.log(e);
} )





function getPostList(){
  fetch('/api/posts/')
  .then(res => res.json())
  .then(data =>{
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

function renderPost(post){
  const root = document.getElementById('root');
  const div =createNode('div');
  div.className = 'post-item';
  const title = createNode('h2');
  const content = createNode('p');
  const publishDate = createNode('span');
  const lastUpdated = createNode('span');
  const author = createNode('small');

  author.innerText = post.author;
  title.innerText = `${post.title} written by ${post.author}`;

  content.innerText = post.content;
  publishDate.innerText = `Published :${new Date(post.publish_date).toUTCString()}`;
  lastUpdated.innerText = `Last Updated :${new Date(post.updated).toUTCString()}`;

  append(div,title);
  append(div,content);
  append(div,publishDate);
  append(div,lastUpdated);
  append(root,div);

}

getPostList()

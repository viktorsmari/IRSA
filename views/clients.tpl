%include('index.tpl', title='Pagaaaa')
<h2>Clients</h2>

% setdefault('text', 'Fann ekki text')
% setdefault('author','fann ekki author')

<p> {{ get('title', 'No Title') }} </p>
<p> {{ text }} </p>

% if defined('author'):
  <p>{{ author }}</p>
% end
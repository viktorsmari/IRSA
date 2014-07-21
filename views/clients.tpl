%include('index.tpl')
<h2>Clients</h2>

<table class="table table-striped table-bordered table-hover table-condensed">
<thead>
	<tr>
		<th>ID</th>
		<th>Name</th>
		<th>SSN</th>
		<th>Email</th>
		<th>Phone</th>
		<th>Address</th>
		<th>Postbox</th>
	</tr>
</thead>
<tbody>
%for row in rows:
	<tr>
	%for col in row:
		<td>{{col}}</td>
	%end
	</tr>

%end
</tbody>
</table> 


%include('footer.tpl')
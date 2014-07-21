%include('index.tpl', title='Pagaaaa')
<h2>Overview</h2>

<table class="table table-striped table-bordered table-hover table-condensed">
<thead>
	<tr>
		<th>ID</th>
		<th>Serial</th>
		<th>Client</th>
		<th>Status</th>
		<th>Make</th>
		<th>Color</th>
		<th>ProblemDescr</th>
		<th>SolutionDesc</th>
		<th>ShortDesc</th>
		<th>EnteredBy</th>
		<th>AssignedTo</th>
		<th>Received</th>
		<th>Started</th>
		<th>Finished</th>
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
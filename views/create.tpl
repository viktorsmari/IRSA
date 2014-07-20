%include('index.tpl', title='Pagaaaa')

	<div class="row">
		<h2>Create</h2>
	</div>
	<hr>

	<form class="form-horizontal" role="form" action="/new" method="GET">
		<div class="form-group has-success has-feedback">
			<div class="row">
				<div class="col-md-5 col-xs-5">
					<div class="col-md-12">
						<h4>Client info</h4>
					</div>
					<div class="col-md-4 col-xs-6">
						<label class="control-label" for="">SSN </label>
					</div>
					<div class="col-md-8">
						<input name="ssn" type="text" class="form-control" id="inputSuccess4">
						<span class="glyphicon glyphicon-ok form-control-feedback"></span>
						<!-- Glyphicon not loading, must be loaded via /static ? -->
					</div>

					<div class="col-md-4 col-xs-6">
						<label class="control-label" for=""> Name</label>
					</div>
					<div class="col-md-8">
						<input name="name" type="text" class="form-control" id="inputSuccess4">
					</div>

					<div class="col-md-4 col-xs-6">
						<label class="control-label" for=""> Phone</label>
					</div>
					<div class="col-md-8">
						<input name="phone" type="text" class="form-control" id="inputSuccess4">
					</div>

					<div class="col-md-4 col-xs-6">
						<label class="control-label" for=""> Email</label>
					</div>
					<div class="col-md-8">
						<input name="email" type="text" class="form-control" id="inputSuccess4">
					</div>
					
					<div class="col-md-4 col-xs-6">
						<label class="control-label" for=""> Address</label>
					</div>
					<div class="col-md-8">
						<input name="address" type="text" class="form-control" id="inputSuccess4">
					</div>
					<div class="col-md-4 col-xs-6">
						<label class="control-label" for=""> PO BOX</label>
					</div>
					<div class="col-md-8">
						<input name="pobox" type="text" class="form-control" id="inputSuccess4">
					</div>
					<div class="col-md-12">
						<h4>Bicycle info</h4>
					</div>
					<div class="col-md-4 col-xs-6">
						<label class="control-label" for=""> Ready Date</label>
					</div>
					<div class="col-md-8">
						<input type="text" class="form-control" id="inputSuccess4">
					</div>
					<div class="col-md-12">
					</div>

					<div class="col-md-4 col-xs-6">
						<label class="control-label" for=""> Serial Number</label>
					</div>
					<div class="col-md-8">
						<input type="text" class="form-control" id="inputSuccess4">
					</div>

					<div class="col-md-4 col-xs-6">
						<label class="control-label" for=""> Brand</label>
					</div>
					<div class="col-md-8">
						<select class="form-control">
							<option></option>
						</select>
					</div>

					<div class="col-md-4 col-xs-6">
						<label class="control-label" for="">Type</label>
					</div>
					<div class="col-md-8">
						<input type="text" class="form-control" id="inputSuccess4">
					</div>

					<div class="col-md-4 col-xs-4">
						<label class="control-label" for="">Color </label>
					</div>
					<div class="col-md-8">
						<select class="form-control">
							<option></option>
						</select>

					</div>

				</div> <!-- end Left form -->

				<div class="col-md-7 col-xs-7">
					<textarea class="form-control" rows="15"></textarea>
					<input class="btn btn-primary btn-lg" type='submit' name="save" value="Save">
				</div> <!-- End right form -->

			</div> <!-- End row -->
		</div> <!-- End form group -->
	</form>

% include('footer.tpl')
package no.uio.ifi.pascal2100.parser;
import no.uio.ifi.pascal2100.main.*;
import no.uio.ifi.pascal2100.scanner.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import java.util.ArrayList;

public class FuncDecl extends PascalDecl {

	
	Block b;
	Block b2;
	public ParamDeclList pdl;
	TypeName tn;
	public  String name;
	public FuncDecl nextfunc;
	public ArrayList <FuncDecl> funcdecllist = new ArrayList<FuncDecl>();
	
	public FuncDecl(String id, int lNum) {
		super(id, lNum);
		// TODO Auto-generated constructor stub
	}
	
	/**
     * Parse a FuncDecl.
     * @param Scanner Tokens.
     * @return the FuncDecl object of the parse tree.
     * function-- name-- param decl list--- :--- type name--- ;--- block--- ;-----
     */

	public static FuncDecl parse(Scanner s) {
		// TODO Auto-generated method stub
		enterParser("func decl");
		s.skip(functionToken);
		s.test(nameToken);
		FuncDecl fd= new FuncDecl(s.curToken.id,s.curLineNum());
		fd.name=s.curToken.id;
		s.readNextToken();
		System.out.println("check kind"+ s.curToken.kind);
		if(s.curToken.kind==leftParToken){
		fd.pdl=ParamDeclList.parse(s);fd.pdl.fndecl=fd;
		}
		
		s.skip(colonToken);
		fd.tn=TypeName.parse(s);
		s.skip(semicolonToken);
		fd.b2=Block.parse(s);
		
		s.skip(semicolonToken);
		leaveParser("func decl");
		
		return fd;
	}
	
		@Override public String identify() {
			return "<func decl> " +name+ " on line " + lineNum;
			
	}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		Main.log.prettyPrintLn();
		Main.log.prettyOutdent();
		Main.log.prettyOutdent();
		Main.log.prettyOutdent();
		Main.log.prettyPrint(" function ");Main.log.prettyPrint(name);
		if (pdl!= null){
			pdl.prettyPrint();
			}
		Main.log.prettyPrint(": ");
		if (tn!=null)tn.prettyPrint();
		Main.log.prettyPrint(";");
		if (b2!=null)b2.prettyPrint();
		Main.log.prettyPrintLn(";");
		Main.log.prettyPrintLn();
		Main.log.prettyPrintLn();
		Main.log.prettyPrintLn();
		
	}

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		curScope.decls.put(name, this);
		if (pdl!= null){
			pdl.check(curScope,lib);
			 for (ParamDecl pd : pdl.paramdecls){
				
				curScope.addDecl(pd.name,pd);
			}
			}
		if (tn!=null)tn.check(curScope,lib);
		if(b2!=null) {
			b2.outerScope= curScope;
			b2.check(curScope, lib);
		}
		
	}

	

}